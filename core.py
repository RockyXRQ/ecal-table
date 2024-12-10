import typing

from ecal.core import core as ecal_core
from ecal.core import service as ecal_service
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from google.protobuf.message import Message

_has_ecal_init: bool = False


def init(argv: list[str], name: str):
    global _has_ecal_init
    if not _has_ecal_init:
        ecal_core.initialize(argv, name)
        _has_ecal_init = True


class _PingClient:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.has_pong: bool = False
        self.client: ecal_service.Client = ecal_service.Client(name)
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


_ping_clients: dict[str, _PingClient] = {}


def ping(name: str) -> bool:
    if name not in _ping_clients:
        _ping_clients[name] = _PingClient(name)
    _ping_clients[name].ping()


def has_pong(name: str) -> bool:
    if name not in _ping_clients:
        return False
    return _ping_clients[name].has_pong


class Table:
    """
    Manages Entry objects with unique keys and message classes. Ensures eCAL is initialized
    """

    class _PongServer:
        def __init__(self, name: str) -> None:
            self.name: str = name
            self.server: ecal_service.Server = ecal_service.Server(name)
            self.server.add_method_callback(
                "ping", "ping_type", "pong_type", self._callback
            )

        def _callback(self, method_name, req_type, resp_type, request) -> None:
            return 0, bytes("pong", "ascii")

        def destroy(self) -> None:
            self.server.destroy()

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

        def get_msg(self, default: Message) -> (Message, float):
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

        def get_val(self, default: typing.Any) -> (typing.Any, float):
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
    _pong_server: dict[str, _PongServer] = {}
    _inst_count: int = 0

    def __init__(self, name: str, root: str = ""):
        """
        Initializes the Table and eCAL
        :param name: name for the eCAL process
        :param root: root for the entry keys
        """
        self._name = name
        if self._name not in self._pong_server:
            self._pong_server[self._name] = self._PongServer(self._name)
        self._inst_count += 1
        self._root = root

    def ok(self) -> bool:
        """
        eCAL process state
        :return: eCAL process state
        """
        return ecal_core.ok()

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

    def finalize(self) -> None:
        """
        Finalizes the Table and eCAL
        """
        if self._name in self._pong_server:
            self._pong_server[self._name].destroy()
            del self._pong_server[self._name]

        self._inst_count -= 1
        if self._inst_count == 0:
            ecal_core.finalize()
