from flask import Flask
from markupsafe import escape

# Create app instance 
app = Flask(__name__)


@app.route('/')
def hello_workshop():
    return "<h1>Welcome to Web2biz. Team<h1>"


@app.route('/hello')
def say_hello():
    return "hello from hello route"

# route path varibale

@app.route('/hello/<username>')
def say_hello_to_user(username):
    return 'Hello %s' % escape(username)

