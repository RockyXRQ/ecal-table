import sys
import time

import core

if __name__ == "__main__":
    instance = core.Instance(sys.argv, "rec")
    
    while True:
        print("************Received************")
        print(f"int: {instance.getInt('test_int')}")
        print(f"double: {instance.getDouble('test_double')}")
        print(f"str: {instance.getStr('test_str')}")
        print(f"bool: {instance.getBool('test_bool')}")
        print("****************************")
        print("")


        time.sleep(1)

