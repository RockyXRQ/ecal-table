# [eCAL](https://eclipse-ecal.github.io/ecal/) Table

A simple wrapper for [eCAL](https://eclipse-ecal.github.io/ecal/) pub/sub with protobuf messages.

## Quick Start

```python
import sys
import core
import proto

# Initialize table with sys.argv
table = core.Table(sys.argv, "demo")

# Basic types (Bool/Int/Double/Str) with single 'val' field
# Use get_val/set_val
table.entry("my_int", proto.Int).set_val(42)
val = table.entry("my_int", proto.Int).get_val(default=0)

# Complex types
# Use get_msg/set_msg
example_msg = proto.Example(val_1="hello", val_2=123)
table.entry("my_msg", proto.Example).set_msg(example_msg)
msg = table.entry("my_msg", proto.Example).get_msg(default=proto.Example())

# Subscribe with callback
table.entry("my_int", proto.Int).set_callback(lambda key, msg, time: print(f"Got: {msg.val}"))
```

## Examples

Run sender:

```shell
python3 -m example.snd
```

Run receiver (choose one):

```shell
python3 -m example.rec      # polling
python3 -m example.rec_cb   # callback
```

## Development

Proto files are automatically compiled to Python when saved. The workflow:

1. Edit `.proto` files in `proto/src/`
2. Save triggers:
   - Generate `*_pb2.py` files
   - Update `proto/__init__.py`
