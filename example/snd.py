"""
Example sender that publishes various message types:
- Basic types (Int/Double/Str/Bool) using set_val()
- Complex type (Example) using set_msg()

Messages are published every second with incrementing/alternating values.
"""

import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "snd")

    # Initialize values
    int_val = 1
    double_val = 2.0
    str_val = "Hello"
    bool_val = True
    example_msg = proto.Example(val_1="LALALA", val_2=32123)

    try:
        while table.ok():
            # Publish all messages
            table.entry("test_int", proto.Int).set_val(int_val)
            table.entry("test_double", proto.Double).set_val(double_val)
            table.entry("test_str", proto.Str).set_val(str_val)
            table.entry("test_bool", proto.Bool).set_val(bool_val)
            table.entry("test_msg", proto.Example).set_msg(example_msg)

            # Print current values
            print(f"int: {int_val}")
            print(f"double: {double_val}")
            print(f"str: {str_val}")
            print(f"bool: {bool_val}")
            print(f"example: {example_msg}")
            print("")

            # Update values for next iteration
            int_val += 1
            double_val += 1.0
            str_val += "!"
            bool_val = not bool_val

            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
