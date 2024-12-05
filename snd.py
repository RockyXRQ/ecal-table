import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "snd")

    int_val = 1
    double_val = 2.0
    str_val = "Hello"
    bool_val = True
    resolution_msg = proto.Resolution(width=1920, height=1080, fps=33)

    while True:
        table.entry("test_int", proto.Int).set_val(int_val)
        table.entry("test_double", proto.Double).set_val(double_val)
        table.entry("test_str", proto.Str).set_val(str_val)
        table.entry("test_bool", proto.Bool).set_val(bool_val)
        table.entry("test_resolution", proto.Resolution).set_msg(resolution_msg)

        print("************Sent************")
        print(f"int: {int_val}")
        print(f"double: {double_val}")
        print(f"str: {str_val}")
        print(f"bool: {bool_val}")
        print(f"resolution: {resolution_msg}")
        print("****************************")
        print("")

        int_val += 1
        double_val += 1.0
        str_val += "!"
        bool_val = not bool_val

        time.sleep(1)
