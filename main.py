import time
from flask import Flask

import redis

r = redis.Redis(
    host='127.0.0.1',
    port=6379)

app = Flask(__name__)


@app.route("/<x>")
def hello_world(x):

    if not r.exists(x):

        result = int(x) + 1
        time.sleep(5)
        r.set(x, str(result))
        return str(result)

    else:
        return str(r.get(x))

