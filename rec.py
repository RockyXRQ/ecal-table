import sys
import time

import core
from proto import capture_pb2

if __name__ == "__main__":
    instance = core.Instance(sys.argv, "rec")

    while True:
        print("************Received************")
        print(f"int: {instance.get_int('test_int')}")
        print(f"double: {instance.get_double('test_double')}")
        print(f"str: {instance.get_str('test_str')}")
        print(f"bool: {instance.get_bool('test_bool')}")
        print(
            f"resolution: {instance.get_resolution('test_resolution', capture_pb2.Resolution(width=111, height=0, fps=0))}"
        )
        print("****************************")
        print("")

        time.sleep(1)
