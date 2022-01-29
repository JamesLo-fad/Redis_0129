import time
from flask import Flask

import redis

r = redis.Redis(
    host='10.182.0.2',
    port=6379)

app = Flask(__name__)


@app.route("/<x>")
def hello_world(x):

    if not r.exist(x):

        result = x + 1
        time.sleep(5)
        return result
        r.set(result)

    else:
        r.get(x)
