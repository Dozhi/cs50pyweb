from flask import Flask , render_template , request
app = Flask(__name__)

'''
@app.route('/')
def hello_world():
    return 'Hello, World!'
'''
@app.route('/')
def index():
	name = request.args.get("name")
	return render_template("acc.html" , name=name)

@app.route('/hello')
def hello():
	return "hello!"
@app.route('/bye')
def bye():
	return 'bye'

@app.route('/user/<username>')
def show_user_profile(username):
	#show user profile 
	return 'User : %s ' % username

@app.route('/id/<int:post_id>')
def show_post_id(post_id):
	return 'Post id : %d' % show_post_id

@app.route("/profile/<name>")
def profile(name):
	return render_template("profile.html" , name=name)


if __name__ =="__main__":
	app.run()