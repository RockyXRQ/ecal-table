import sys
import time

import core

if __name__ == "__main__":
    core.init(sys.argv, "ping_client")

    try:
        while core.ok():
            core.ping("pong_server")
            print(core.has_pong("pong_server"))
            time.sleep(1)
    except KeyboardInterrupt:
        print("Stopping...")
        core.finalize()
