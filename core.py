import typing

from ecal.core import core as ecal_core
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from google.protobuf.message import Message


class Entry:
    def __init__(self, key: str, msg_clazz: typing.Type[Message]):
        self.key = key
        self.msg_clazz = msg_clazz

        self.pub: ProtoPublisher = None
        self.sub: ProtoSubscriber = None

    def _lazy_init_pub(self):
        if self.pub is None:
            self.pub = ProtoPublisher(self.key, self.msg_clazz)

    def _lazy_init_sub(self):
        if self.sub is None:
            self.sub = ProtoSubscriber(self.key, self.msg_clazz)

    def set_msg(self, msg: Message):
        self._lazy_init_pub()
        self.pub.send(msg)

    def get_msg(self, default: Message) -> (Message, float):
        self._lazy_init_sub()
        ret, msg, timestamp = self.sub.receive()
        return msg if ret > 0 else default, timestamp

    def set_val(self, val: typing.Any):
        self._lazy_init_pub()
        self.pub.send(self.msg_clazz(val=val))

    def get_val(self, default: typing.Any) -> (typing.Any, float):
        self._lazy_init_sub()
        ret, msg, timestamp = self.sub.receive()
        return msg.val if ret > 0 else default, timestamp

    def set_callback(self, callback: typing.Callable[[str, Message, float], None]):
        self._lazy_init_sub()
        self.sub.set_callback(callback)

    def rm_callback(self, callback: typing.Callable[[str, Message, float], None]):
        self.sub.rem_callback(callback)


class Table:
    _has_ecal_init: bool = False
    _entries: dict[str, Entry] = {}

    def __init__(self, argv: list[str], name: str):
        if not self._has_ecal_init:
            self._has_ecal_init = True
            ecal_core.initialize(argv, name)

    def entry(self, key: str, msg_clazz: typing.Type[Message]) -> Entry:
        if key not in self._entries:
            self._entries[key] = Entry(key, msg_clazz)
        return self._entries[key]
