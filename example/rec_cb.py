"""
Example receiver that uses callbacks for message handling:
- Basic types (Int/Double/Str/Bool) using set_callback()
- Complex type (Example) using set_callback()

This demonstrates the callback approach to receiving messages.
Each message type has its own callback that prints the received value.
"""

import sys
import time

import core
import proto

if __name__ == "__main__":
    table = core.Table(sys.argv, "rec_cb")

    # Set up callbacks for all message types
    table.entry("test_int", proto.Int).set_callback(
        lambda key, msg, timestamp: print(f"int: {msg.val}")
    )
    table.entry("test_double", proto.Double).set_callback(
        lambda key, msg, timestamp: print(f"double: {msg.val}")
    )
    table.entry("test_str", proto.Str).set_callback(
        lambda key, msg, timestamp: print(f"str: {msg.val}")
    )
    table.entry("test_bool", proto.Bool).set_callback(
        lambda key, msg, timestamp: print(f"bool: {msg.val}")
    )
    table.entry("test_msg", proto.Example).set_callback(
        lambda key, msg, timestamp: print(f"example: {msg}")
    )

    try:
        # Keep program running to receive callbacks
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
