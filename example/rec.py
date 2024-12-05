import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "rec")

    try:
        while True:
            print(f"int: {table.entry('test_int', proto.Int).get_val(0)}")
            print(f"double: {table.entry('test_double', proto.Double).get_val(0)}")
            print(f"str: {table.entry('test_str', proto.Str).get_val('')}")
            print(f"bool: {table.entry('test_bool', proto.Bool).get_val(False)}")
            print(
                f"example: {table.entry('test_msg', proto.Example).get_msg(proto.Example(val_1='xixixi', val_2=12321))}"
            )
            print("")

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
