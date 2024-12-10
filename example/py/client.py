import sys
import time

import core

if __name__ == "__main__":
    core.init(sys.argv, "ping_test_process")

    while True:
        core.ping("pong_server")
        print(core.has_pong("pong_server"))
        time.sleep(1)
