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
        volumes={'D:/dev/my-docker/docker_app/': {'bind': '/var/log/', 'mode': 'rw'}},
        detach=True,
    )
    return redis_container, publisher_container, subscriber_container


if __name__ == '__main__':
    # subscriber_image, _ = client.images.build(path='docker_app', tag='subscriber', buildargs={'app': 'sub_app.py'})
    # print(subscriber_image, 'build DONE')
    # publisher_image,  _ = client.images.build(path='docker_app', tag='publisher', buildargs={'app': 'pub_app.py'})
    # print(publisher_image, 'build DONE')
    cnt_ids = run_containers(client, 'redis:latest', 'subscriber', 'publisher')
    print('> DONE', cnt_ids)
    # os.system(f'async_watchdog.py {" ".join(cnt_ids)}')
