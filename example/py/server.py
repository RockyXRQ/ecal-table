import sys
import time

import core

if __name__ == "__main__":
    core.init(sys.argv, "pong_server")

    try:
        while core.ok():
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        core.finalize()
