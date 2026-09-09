#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index1():
    return "Hello, World!"

@app.route('/index2')
def index2():
    return "Hello, World2!"

if __name__ == '__main__':
    app.run(debug = True)