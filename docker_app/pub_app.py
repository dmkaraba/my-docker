import os
import sys
import redis
import logging
from flask import Flask, request, jsonify


app = Flask(__name__)
r = redis.Redis(host=os.environ['APP_REDIS_HOST'], port=os.environ['APP_REDIS_PORT'], db=0)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


@app.route('/healthcheck', methods=['GET'])
def healthcheck():
    return jsonify(status=0)


@app.route('/v1/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/v1/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    msg = '{r.host} {r.method} {r.url}'.format(r=request)
    logger.info(msg)
    r.publish(os.environ['APP_REDIS_CHANNEL'], msg)
    return jsonify(msg=msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
