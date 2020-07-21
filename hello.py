from flask import Flask

# Create app instance 
app = Flask(__name__)


@app.route('/')
def hello_workshop():
    return "Welcome to Web2biz. Team"