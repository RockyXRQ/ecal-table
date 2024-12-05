import typing

from ecal.core import core as ecal_core
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber
from google.protobuf.message import Message

from proto import basic_pb2, capture_pb2


class Entry:
    def __init__(self, key: str, clazz: typing.Type[Message]):
        self.pub = ProtoPublisher(key, clazz)
        self.sub = ProtoSubscriber(key, clazz)

    def send(self, val: typing.Any, timestamp: float = -1):
        self.pub.send(val, timestamp)

    def recv(self) -> (bool, typing.Any, float):
        return self.sub.receive()

    def set_recv_callback(
        self, callback: typing.Callable[[str, typing.Any, float], None]
    ):
        self.sub.set_callback(callback)


class Instance:
    _has_ecal_init: bool = False
    _entries: dict[str, Entry] = {}

    def __init__(self, argv: list[str], name: str):
        if not self._has_ecal_init:
            self._has_ecal_init = True
            ecal_core.initialize(argv, name)

    def _create_entry(self, key: str, clazz: typing.Any):
        if key not in self._entries:
            self._entries[key] = Entry(key, clazz)

    def _set_basic(
        self,
        key: str,
        val: int | float | str | bool,
        clazz: typing.Type[
            basic_pb2.Int | basic_pb2.Double | basic_pb2.String | basic_pb2.Bool
        ],
    ):
        self._create_entry(key, clazz)
        msg = clazz(val=val)
        self._entries[key].send(msg)

    def _get_basic(
        self,
        key: str,
        default: int | float | str | bool,
        clazz: typing.Type[
            basic_pb2.Int | basic_pb2.Double | basic_pb2.String | basic_pb2.Bool
        ],
    ) -> (int | float | str | bool, float):
        self._create_entry(key, clazz)
        ret, msg, timestamp = self._entries[key].recv()
        return msg.val if ret > 0 else default, timestamp

    def set_int(self, key: str, val: int):
        self._set_basic(key, val, basic_pb2.Int)

    def get_int(self, key: str, default: int = 0) -> (int, float):
        return self._get_basic(key, default, basic_pb2.Int)

    def set_double(self, key: str, val: float):
        self._set_basic(key, val, basic_pb2.Double)

    def get_double(self, key: str, default: float = 0.0) -> (float, float):
        return self._get_basic(key, default, basic_pb2.Double)

    def set_str(self, key: str, val: str):
        self._set_basic(key, val, basic_pb2.String)

    def get_str(self, key: str, default: str = "") -> (str, float):
        return self._get_basic(key, default, basic_pb2.String)

    def set_bool(self, key: str, val: bool):
        self._set_basic(key, val, basic_pb2.Bool)

    def get_bool(self, key: str, default: bool = False) -> (bool, float):
        return self._get_basic(key, default, basic_pb2.Bool)

    def _set_proto(self, key: str, msg: Message, clazz: typing.Type[Message]):
        self._create_entry(key, clazz)
        self._entries[key].send(msg)

    def _get_proto(self, key: str, default: Message, clazz: typing.Type[Message]):
        self._create_entry(key, clazz)
        ret, msg, timestamp = self._entries[key].recv()
        return msg if ret > 0 else default, timestamp

    def set_resolution(self, key: str, msg: capture_pb2.Resolution):
        self._set_proto(key, msg, capture_pb2.Resolution)

    def get_resolution(
        self, key: str, default: capture_pb2.Resolution
    ) -> (capture_pb2.Resolution, float):
        return self._get_proto(key, default, capture_pb2.Resolution)
