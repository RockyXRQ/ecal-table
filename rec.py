import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "rec")

    while True:
        print("************Received************")
        print(f"int: {table.entry('test_int', proto.Int).get_val(0)}")
        print(f"double: {table.entry('test_double', proto.Double).get_val(0)}")
        print(f"str: {table.entry('test_str', proto.Str).get_val('')}")
        print(f"bool: {table.entry('test_bool', proto.Bool).get_val(False)}")
        print(
            f"resolution: {table.entry('test_resolution', proto.Resolution).get_msg(proto.Resolution(width=111, height=0, fps=0))}"
        )
        print("****************************")
        print("")

        time.sleep(1)
