# eCAL Table

Lightweight wrapper for [eCAL](https://eclipse-ecal.github.io/ecal/) pub/sub with Protocol Buffers integration.

## Usage

```python
import sys

import core
import proto

# Initialize eCAL runtime
core.init(sys.argv, "demo")
table = core.Table()

# Basic types with single value field
entry = table.entry(proto.Int, "counter")
entry.set_val(42)
value = entry.get_val(default=0)

# Custom message types
msg = proto.Example(val_1="hello", val_2=123)
entry = table.entry(proto.Example, "status")
entry.set_msg(msg)
received = entry.get_msg(default=proto.Example())

# Callback-based subscription
entry.set_callback(lambda topic, msg, time: print(f"Received: {msg.val}"))

# Process monitoring
core.ping("target_process")
is_alive = core.has_pong("target_process")
```

## Examples

### Python

Run pub/sub:
```bash
python3 -m example.py.snd            # sender
python3 -m example.py.rec            # polling
python3 -m example.py.rec_cb         # callback
```

Run process monitoring:
```bash
python3 -m example.py.server         # pong server
python3 -m example.py.client         # ping client
```

### C++

Build:
```bash
cd example/cpp
mkdir build && cd build
cmake ..
make
```

Run examples:
```bash
./snd       # sender
./rec       # polling
./rec_cb    # callback
```

## Development

Proto files are automatically compiled when saved(by VSCode `Run on Save` extension):

1. Edit `.proto` files in `proto/src/`
2. Save triggers:
   - Generate Python `*_pb2.py` files in `proto/py/`
   - Generate C++ `.pb.h` and `.pb.cc` files in `proto/cpp/`
   - Update `proto/__init__.py`
