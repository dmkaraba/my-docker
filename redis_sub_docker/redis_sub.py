import time
import redis


r = redis.Redis(host='redis', port=6379, db=0)
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe('flask-channel')


def main_loop():
    with open('/logs/log.txt', 'a+') as f:
        while True:
            message = p.get_message()
            if message:
                print(message)
                f.write(f'{message["data"]}\n')
                f.flush()
            time.sleep(0.001)


if __name__ == '__main__':
    main_loop()
