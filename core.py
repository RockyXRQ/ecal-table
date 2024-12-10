import typing

from ecal.core import core as ecal_core
from ecal.core import service as ecal_service
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from google.protobuf.message import Message


class _PingClient:
    """
    Handles outgoing ping requests for eCAL process monitoring
    """

    def __init__(self, process_name: str) -> None:
        self.name: str = process_name
        self.has_pong: bool = False
        self.client: ecal_service.Client = ecal_service.Client(process_name)
        self.client.add_response_callback(self._callback)

    def _callback(self, service_info, response) -> None:
        if service_info["call_state"] == "call_state_executed":
            self.has_pong = True
        else:
            self.has_pong = False

    def ping(self) -> None:
        self.client.call_method("ping", b"ping")

    def destroy(self) -> None:
        self.client.destroy()


class _PongServer:
    """
    Provides ping-pong service response for process health checks
    """

    def __init__(self, process_name: str) -> None:
        self.name: str = process_name
        self.server: ecal_service.Server = ecal_service.Server(process_name)
        self.server.add_method_callback(
            "ping", "ping_type", "pong_type", self._callback
        )

    def _callback(self, method_name, req_type, resp_type, request) -> None:
        return 0, bytes("pong", "ascii")

    def destroy(self) -> None:
        self.server.destroy()


_has_ecal_init: bool = False
_ping_clients: dict[str, _PingClient] = {}
_pong_servers: dict[str, _PongServer] = {}


def init(argv: list[str], process_name: str) -> None:
    """
    Initializes eCAL runtime and pong server
    :param argv: command line arguments
    :param process_name: process name for identification
    """
    global _has_ecal_init
    if not _has_ecal_init:
        ecal_core.initialize(argv, process_name)
        _has_ecal_init = True
    if process_name not in _pong_servers:
        _pong_servers[process_name] = _PongServer(process_name)


def ok() -> bool:
    """
    eCAL runtime state
    :return: eCAL runtime state
    """
    return ecal_core.ok()


def finalize() -> None:
    """
    Performs eCAL cleanup and resource deallocation
    """
    for server in _pong_servers.values():
        server.destroy()
    for client in _ping_clients.values():
        client.destroy()
    ecal_core.finalize()


def ping(process_name: str) -> None:
    """
    Initiates a ping request
    :param process_name: target process name
    """
    if process_name not in _ping_clients:
        _ping_clients[process_name] = _PingClient(process_name)
    _ping_clients[process_name].ping()


def has_pong(process_name: str) -> bool:
    """
    Verifies ping response status
    :param process_name: target process name
    :return: response status
    """
    if process_name not in _ping_clients:
        return False
    return _ping_clients[process_name].has_pong


class Table:
    """
    Manages message routing through Entry objects
    """

    class Entry:
        """
        Manages a publisher and subscriber for a specific key and message class
        """

        def __init__(self, key: str, msg_class: typing.Type[Message]) -> None:
            """
            :param key: unique entry identifier
            :param msg_class: protobuf message class type
            """
            self.key: str = key
            self.msg_class: typing.Type[Message] = msg_class
            self.pub: ProtoPublisher | None = None
            self.sub: ProtoSubscriber | None = None

        def _lazy_init_pub(self) -> None:
            """Initializes the publisher if needed"""
            if self.pub is None:
                self.pub = ProtoPublisher(self.key, self.msg_class)

        def _lazy_init_sub(self) -> None:
            """Initializes the subscriber if needed"""
            if self.sub is None:
                self.sub = ProtoSubscriber(self.key, self.msg_class)

        def set_msg(self, msg: Message) -> None:
            """
            Sends a Protobuf message
            :param msg: protobuf message to send
            """
            self._lazy_init_pub()
            self.pub.send(msg)

        def get_msg(self, default: Message) -> tuple[Message, float]:
            """
            Receives a Protobuf message
            :param default: default protobuf message if none received
            :return: protobuf message and timestamp
            """
            self._lazy_init_sub()
            ret, msg, timestamp = self.sub.receive()
            return msg if ret > 0 else default, timestamp

        def set_val(self, val: typing.Any) -> None:
            """
            Sends a value by creating a Protobuf message instance
            :param val: value to send
            """
            self._lazy_init_pub()
            self.pub.send(self.msg_class(val=val))

        def get_val(self, default: typing.Any) -> tuple[typing.Any, float]:
            """
            Receives a value
            :param default: default value if none received
            :return: value and timestamp
            """
            self._lazy_init_sub()
            ret, msg, timestamp = self.sub.receive()
            return msg.val if ret > 0 else default, timestamp

        def set_callback(
            self, callback: typing.Callable[[str, Message, float], None]
        ) -> None:
            """
            Sets a callback function that will be triggered when receiving Protobuf messages
            :param callback: Function to be called when a message is received. The callback takes:
                            - topic name (str)
                            - received Protobuf message (Message)
                            - timestamp (float)
            """
            self._lazy_init_sub()
            self.sub.set_callback(callback)

        def rm_callback(
            self, callback: typing.Callable[[str, Message, float], None]
        ) -> None:
            """
            Removes a previously set callback
            :param callback: function to remove
            """
            self.sub.rem_callback(callback)

    _entries: dict[str, Entry] = {}

    def __init__(self, root: str = "") -> None:
        """
        Initializes the Table and eCAL
        :param root: root for the entry keys
        """
        self._root = root

    def entry(self, msg_class: typing.Type[Message], key: str) -> Entry:
        """
        Retrieves or creates an Entry
        :param msg_class: protobuf message class type
        :param key: unique identifier for the entry
        :return: the Entry object
        """
        full_key = f"{self._root.replace('/', '')}/{key}"
        if full_key not in self._entries:
            self._entries[full_key] = self.Entry(full_key, msg_class)
        return self._entries[full_key]
