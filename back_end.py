from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1> Hello World!</h1>'

@app.route('/users/<name>')
def user(name):
    return '<h1>hello, {}!</h1>'.format(name)
