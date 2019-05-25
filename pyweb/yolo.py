from flask import Flask , render_template ,request


app=Flask(__name__)


@app.route('/')
def index():
	return "blabllalala welcome to index"


@app.route('/login')
def login():
	name =request.args.get("name" , "Error : No name input")
	password =request.args.get("password" , "Error : No password input")
	gender =request.args.get("gender" , "no gender")
	return render_template('login.html' , name=name , password=password , gender=gender) 


@app.route('/register' , methods=["POST"])
def register():
	name =request.args.get('name')
	password =request.args.get('password')
	gender =request.args.get('gender')
	if not name or not password:
		return "failed"
	return render_template('register.html' , name=name , password=password , gender=gender)








'''
@app.route("/")
def index():
	name = request.args.get("name" , "no name")
	if name is "dozhi":
		name = "pydars"
	return render_template("profile.html" , name=name)


@app.route('/userid/<int:id>')
def user(id):
	return "user: %d" % id


@app.route('/profile/<name>')
def profile_name(name):
	return render_template("profile.html" , name=name)
'''
if __name__=="__main__":
 	app.run()