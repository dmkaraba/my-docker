import os
import docker


client = docker.from_env()

def run_containers(client, redis_name, subscriber_name, publisher_name):
    redis_container = client.containers.run(
        image=redis_name,
        name='redis-cnt',
        detach=True
    )
    publisher_container = client.containers.run(
        image=publisher_name,
        name='pub-app',
        links={'redis-cnt': 'redis'},
        ports={'5000/tcp': '5000'},
        detach=True,
    )
    subscriber_container = client.containers.run(
        image=subscriber_name,
        name='sub-app',
        links={'redis-cnt': 'redis'},
        volumes={'D:/dev/my-docker/subscriber/': {'bind': '/var/log/', 'mode': 'rw'}},
        detach=True,
    )
    return redis_container.id, publisher_container.id, subscriber_container.id


if __name__ == '__main__':
    subscriber_image, _ = client.images.build(path='./subscriber', tag='subscriber:test')
    print(subscriber_image, 'build DONE')
    publisher_image,  _ = client.images.build(path='./publisher', tag='publisher:test')
    print(publisher_image, 'build DONE')
    cnt_ids = run_containers(client, 'redis:latest', subscriber_image.tags[0], publisher_image.tags[0])
    print(cnt_ids, 'run DONE')
    # os.system(f'async_watchdog.py {" ".join(cnt_ids)}')
