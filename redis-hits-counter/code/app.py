from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis-master', port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/health')
def health():
    return 'All fine'

@app.route('/readiness')
def readiness():
    return 'I am ready'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
