from flask import Flask
from markupsafe import escape
from flask import render_template

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
    return 'Hello %s' %(username)

@app.route('/hello/<int:id>')
def say_hello_to_id(id):
    return 'Your Id %d' % (id+1)

# make a simple website
@app.route('/projects')
def projects(name=None):
  return render_template('projects.html',name=name)

@app.route('/about')
def about():
    return render_template('about.html')