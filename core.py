import typing

from ecal.core import core as ecal_core
from ecal.core.publisher import ProtoPublisher
from ecal.core.subscriber import ProtoSubscriber

from proto import basic_pb2


class Entry:
    def __init__(self, key:str, clazz:typing.Any):
        self.pub = ProtoPublisher(key, clazz)
        self.sub = ProtoSubscriber(key, clazz)
    
    def send(self, val:typing.Any):
        self.pub.send(val)

    def recv(self) -> typing.Any:
        return self.sub.receive()

    def set_recv_callback(self, callback:typing.Callable[[str, typing.Any, float], None]):
        self.sub.set_callback(callback)


class Instance:
    _has_ecal_init: bool = False
    _entries: dict[str, Entry] = {}

    def __init__(self, argv:list[str], name:str):
        if not self._has_ecal_init:
            self._has_ecal_init = True
            ecal_core.initialize(argv, name)

    def _create_entry(self, key:str, clazz:typing.Any):
        if key not in self._entries:
            self._entries[key] = Entry(key, clazz)

    def setInt(self, key:str, val:int):
        self._create_entry(key, basic_pb2.Int)
        int_msg = basic_pb2.Int()
        int_msg.val = val
        self._entries[key].send(int_msg)

    def getInt(self, key:str, default:int=0) -> int:
        self._create_entry(key, basic_pb2.Int)
        ret, msg, _ = self._entries[key].recv()
        if ret > 0:
            return msg.val
        return default

    def setDouble(self, key:str, val:float):
        self._create_entry(key, basic_pb2.Double)
        double_msg = basic_pb2.Double()
        double_msg.val = val
        self._entries[key].send(double_msg)

    def getDouble(self, key:str, default:float=0.0) -> float:
        self._create_entry(key, basic_pb2.Double)
        ret, msg, _ = self._entries[key].recv()
        if ret > 0:
            return msg.val
        return default

    def setStr(self, key:str, val:str):
        self._create_entry(key, basic_pb2.String)
        str_msg = basic_pb2.String()
        str_msg.val = val
        self._entries[key].send(str_msg)

    def getStr(self, key:str, default:str="") -> str:
        self._create_entry(key, basic_pb2.String)
        ret, msg, _ = self._entries[key].recv()
        if ret > 0:
            return msg.val
        return default

    def setBool(self, key:str, val:bool):
        self._create_entry(key, basic_pb2.Bool)
        bool_msg = basic_pb2.Bool()
        bool_msg.val = val
        self._entries[key].send(bool_msg)

    def getBool(self, key:str, default:bool=False) -> bool:
        self._create_entry(key, basic_pb2.Bool)
        ret, msg, _ = self._entries[key].recv()
        if ret > 0:
            return msg.val
        return default

if __name__ == "__main__":
    pass