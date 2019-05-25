from flask import Flask , request , render_template , redirect

app = Flask(__name__)


#register user
users=[]


@app.route('/')
def index():
	return render_template('login2.html')


@app.route("/registrants")
def registrants():
	return render_template("registredusers.html" , users=users)

@app.route("/register", methods=["POST"])
def register():
	name=request.form.get('name')
	if not name:
		return "failure"
	users.append(f"{name}")
	return redirect('/registrants')

a









if __name__=="__main__":
	app.run()