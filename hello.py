from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<p>Hello World</p>"

@app.route('/user')
def hello_world():
    return "<p>Hello User</p>"

@app.route('/edit')
def hello_world():
    return "<p>User edit</p>"