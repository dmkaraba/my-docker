import os
import docker
import subprocess


client = docker.from_env()

def run_containers(client):
    redis_container = client.containers.run(image='redis', name='my-redis-cnt', detach=True)
    publisher_container = client.containers.run(
        image='publisher', name='pub-app', links={'my-redis-cnt': 'redis'}, ports={'5000/tcp': '5000'}, detach=True)
    subscriber_container = client.containers.run(
        image='subscriber', name='sub-app', links={'my-redis-cnt': 'redis'},
        volumes={'D:/dev/my-docker/redis_sub_docker/logs/': {'bind': '/logs/', 'mode': 'rw'}}, detach=True)
    return redis_container.id, publisher_container.id, subscriber_container.id


if __name__ == '__main__':
    cnt_ids = run_containers(client)
    print(cnt_ids)
    os.system(f'async_watchdog.py {" ".join(cnt_ids)}')

