import sys
import time

import core
from proto import capture_pb2

if __name__ == "__main__":
    instance = core.Instance(sys.argv, "snd")

    int_val = 1
    double_val = 2.0
    str_val = "Hello"
    bool_val = True
    resolution_val = capture_pb2.Resolution(width=1920, height=1080, fps=33)

    while True:
        instance.set_int("test_int", int_val)
        instance.set_double("test_double", double_val)
        instance.set_str("test_str", str_val)
        instance.set_bool("test_bool", bool_val)
        instance.set_resolution("test_resolution", resolution_val)

        print("************Sent************")
        print(f"int: {int_val}")
        print(f"double: {double_val}")
        print(f"str: {str_val}")
        print(f"bool: {bool_val}")
        print(f"resolution: {resolution_val}")
        print("****************************")
        print("")

        int_val += 1
        double_val += 1.0
        str_val += "!"
        bool_val = not bool_val

        time.sleep(1)
