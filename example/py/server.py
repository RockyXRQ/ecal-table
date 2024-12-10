import sys
import time

import core

if __name__ == "__main__":
    core.init(sys.argv, "pong_test_process")

    pong_server = core.Table("pong_server")

    while True:
        time.sleep(1)
