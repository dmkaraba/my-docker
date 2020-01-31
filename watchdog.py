import sys
import docker
from time import sleep


def container_watchdog(container_id):
    client = docker.from_env()
    while True:
        container = client.containers.get(container_id)
        if container.status == 'exited':
            container.restart()
            print(container.name, 'RESTARTING')
        yield container.name, container.status


if __name__ == '__main__':
    tasks = [container_watchdog(cnt_id) for cnt_id in sys.argv[1:]]
    while tasks:
        task = tasks.pop(0)
        next(task)
        tasks.append(task)
        sleep(0.5)
