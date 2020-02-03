import os
import time
import redis


r = redis.Redis(host=os.environ['APP_REDIS_HOST'], port=os.environ['APP_REDIS_PORT'], db=0)
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe(os.environ['APP_REDIS_CHANNEL'])


def main_loop():
    with open('/var/log/log.txt', 'a+') as f:
        while True:
            message = p.get_message()
            if message:
                print(message)
                f.write(f'{message["data"]}\n')
                f.flush()
            time.sleep(0.001)


if __name__ == '__main__':
    main_loop()
