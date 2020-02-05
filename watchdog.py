import sys
import time
import docker


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


if __name__ == '__main__':
    container_watchdog(sys.argv[1:])
