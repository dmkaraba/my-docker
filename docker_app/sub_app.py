import os
import sys
import time
import redis
import signal
import logging


r = redis.Redis(host=os.environ['APP_REDIS_HOST'], port=os.environ['APP_REDIS_PORT'], db=0)
p = r.pubsub(ignore_subscribe_messages=True)
p.subscribe(os.environ['APP_REDIS_CHANNEL'])

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger.addHandler(handler)
handler.setFormatter(formatter)

run = True


def handler_stop_signals(signum, frame):
    global run
    run = False


def main_loop():
    with open('/var/log/log.txt', 'a+') as f:
        while run:
            message = p.get_message()
            if message:
                logger.info(message)
                f.write(f'{message["data"]}\n')
                f.flush()
            time.sleep(0.001)


if __name__ == '__main__':
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)
    main_loop()
