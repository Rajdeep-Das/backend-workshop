from flask import Flask
from markupsafe import escape
from flask import render_template
from flask import redirect, url_for,abort
from flask import jsonify


# Create app instance 
app = Flask(__name__, template_folder='templates')


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
@app.route('/projects/<projectname>')
def projectsroot(projectname=None):
  return render_template('projects.html',projectname=projectname)


@app.route('/about')
def about():
    return render_template('about.html')

# redirects and error
@app.route('/redir')
def redirect_user_to_about():
    return redirect(url_for('about'))

# redirects and error
@app.route('/prj')
def redirect_user_to_projects():
    return redirect(url_for('projects',projectname="test"))

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404  

# json response
@app.route('/api/rajdeep')
def api_test():
    # assume this data come from data base table and we store them into varibales
    name="Rajdeep"
    roll=100
    age=25
    return {
        "name":name,
        "roll":roll,
        "age":age,
    }

@app.route('/api/json')
def api_test_json():
    # assume this data come from data base table and we store them into varibales
    userlist = [
        {
        "name":"Acb",
        "roll":"25",
        "age":"25",
        },
        {
        "name":"xyz",
        "roll":"30",
        "age":"25",
        }
    ]
    return jsonify(userlist=userlist)
    

