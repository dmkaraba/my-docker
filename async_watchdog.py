import sys
import docker
import asyncio


async def container_watchdog(container_id):
    client = docker.from_env()
    while True:
        container = client.containers.get(container_id)
        print(container.name, container.status)
        if container.status == 'exited':
            container.restart()
            print(container.name, 'RESTARTING')
        await asyncio.sleep(0.2)


if __name__ == '__main__':
    ioloop = asyncio.get_event_loop()
    tasks = [ioloop.create_task(container_watchdog(id)) for id in sys.argv[1:]]
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
