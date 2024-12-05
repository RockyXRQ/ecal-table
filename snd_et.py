import sys
import time

import core

if __name__ == "__main__":
    instance = core.Instance(sys.argv, "snd")

    int_val = 1
    double_val = 2.0
    str_val = "Hello"
    bool_val = True

    while True:
        instance.setInt("test_int", int_val)
        instance.setDouble("test_double", double_val)
        instance.setStr("test_str", str_val)
        instance.setBool("test_bool", bool_val)

        print("************Sent************")
        print(f"int: {int_val}")
        print(f"double: {double_val}")
        print(f"str: {str_val}")
        print(f"bool: {bool_val}")
        print("****************************")
        print("")

        int_val += 1
        double_val += 1.0
        str_val += "!"
        bool_val = not bool_val

        time.sleep(1)
