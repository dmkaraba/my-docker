import os
import redis
from flask import Flask, request, jsonify

app = Flask(__name__)
r = redis.Redis(host=os.environ['APP_REDIS_HOST'], port=os.environ['APP_REDIS_PORT'], db=0)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    msg = '{r.host} {r.method} {r.url}'.format(r=request)
    r.publish(os.environ['APP_REDIS_CHANNEL'], msg)
    return jsonify(msg=msg)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
