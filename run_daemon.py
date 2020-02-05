import sys
import time
import docker
from daemon import Daemon


def container_watchdog(cnt_names):
    client = docker.from_env()
    while True:
        containers = [cnt for cnt in client.containers.list() if cnt.name in cnt_names]
        for container in containers:
            print('>', container.name, container.status)
            if container.status == 'exited':
                container.restart()
                print('>>> RESTARTED')
        time.sleep(0.05)


class MyDaemon(Daemon):
    def run(self):
        while True:
            time.sleep(1)


if __name__ == "__main__":
    daemon = MyDaemon('docker-app/daemon.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print("Unknown command")
            sys.exit(2)
        sys.exit(0)
    else:
        print(f"usage: {sys.argv[0]} start|stop|restart")
        sys.exit(2)