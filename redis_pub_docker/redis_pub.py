import redis
from flask import Flask, request, jsonify


app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, db=0)


@app.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@app.route('/<path:path>', methods=['GET', 'POST'])
def catch_all(path):
    msg = '{r.host} {r.method} {r.url}'.format(r=request)
    r.publish('flask-channel', msg)
    return jsonify(msg=msg)
