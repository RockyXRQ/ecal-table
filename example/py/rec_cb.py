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
    core.init(sys.argv, "rec_cb")

    while not core.has_pong("snd"):
        print("Waiting for snd process init...")
        core.ping("snd")
        time.sleep(1)

    table = core.Table()

    # Set up callbacks for all message types
    table.entry(proto.Int, "test_int").set_callback(
        lambda key, msg, timestamp: print(f"int: {msg.val}")
    )
    table.entry(proto.Double, "test_double").set_callback(
        lambda key, msg, timestamp: print(f"double: {msg.val}")
    )
    table.entry(proto.Str, "test_str").set_callback(
        lambda key, msg, timestamp: print(f"str: {msg.val}")
    )
    table.entry(proto.Bool, "test_bool").set_callback(
        lambda key, msg, timestamp: print(f"bool: {msg.val}")
    )
    table.entry(proto.Example, "test_msg").set_callback(
        lambda key, msg, timestamp: print(f"example: {msg}")
    )

    try:
        # Keep program running to receive callbacks
        while core.ok():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        core.finalize()
