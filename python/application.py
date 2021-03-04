from flask import Flask
application = app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Python1!'

if __name__ == '__main__':
    app.run()