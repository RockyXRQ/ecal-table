import typing

from ecal.core import core as ecal_core
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from google.protobuf.message import Message


class Table:
    """
    Manages Entry objects with unique keys and message classes. Ensures eCAL is initialized
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

    _has_ecal_init: bool = False
    _entries: dict[str, Entry] = {}

    def __init__(self, argv: list[str], name: str):
        """
        Initializes the Table and eCAL
        :param argv: command-line arguments for eCAL initialization
        :param name: name for the eCAL process
        """
        if not self._has_ecal_init:
            self._has_ecal_init = True
            ecal_core.initialize(argv, name)

    def ok(self) -> bool:
        """
        eCAL process state
        :return: eCAL process state
        """
        return ecal_core.ok()

    def entry(self, key: str, msg_class: typing.Type[Message]) -> Entry:
        """
        Retrieves or creates an Entry
        :param key: unique identifier for the entry
        :param msg_class: protobuf message class type
        :return: the Entry object
        """
        if key not in self._entries:
            self._entries[key] = self.Entry(key, msg_class)
        return self._entries[key]
