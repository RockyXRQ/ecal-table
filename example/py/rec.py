"""
Example receiver that polls for messages every second:
- Basic types (Int/Double/Str/Bool) using get_val() with defaults
- Complex type (Example) using get_msg() with default message

This demonstrates the polling approach to receiving messages.
"""

import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "rec")

    try:
        while table.ok():
            print(f"int: {table.entry(proto.Int, 'test_int').get_val(0)}")
            print(f"double: {table.entry(proto.Double, 'test_double').get_val(0)}")
            print(f"str: {table.entry(proto.Str, 'test_str').get_val('')}")
            print(f"bool: {table.entry(proto.Bool, 'test_bool').get_val(False)}")
            print(
                f"example: {table.entry(proto.Example, 'test_msg').get_msg(proto.Example(val_1='xixixi', val_2=12321))}"
            )
            print("")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        table.finalize()
