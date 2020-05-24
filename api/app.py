from flask import Flask
from settings import APP_DEBUG, APP_PORT, APP_HOST

app = Flask(__name__)


if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)
