from flask import (Flask,render_template,
					request,redirect,url_for,flash,session)

from database.models import(addUser,addMessage,
	                        checkUser,getMessages)

from passlib.hash import sha256_crypt
from  forms.form import UserForm,MessagesForm
from database import models
from functools import wraps



app = Flask(__name__)
app.secret_key = '@%^&(*9867ahsh)'

#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________


def is_logged_in(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if 'logged_in' in session.keys():
			return f(*args,**kwargs)
		else:
			flash('Unauthorized, please log in', 'danger')
			return redirect(url_for('login'))
	return wrap


@app.route('/')
def index():
	return render_template('home.html')

@app.route('/register',methods=['POST','GET'])
def register():
	form = UserForm(request.form)
	if request.method == 'POST':
		if form.validate():
			name=form.name.data
			username=form.username.data
			email=form.email.data
			password=form.password.data
			addUser(name,username,email,password)
			flash('You are registered and can log in!', 'success')
			return redirect(url_for('index'))
	return render_template('register.html',form=form)


@app.route('/login',methods=['GET','POST'])
def login():
	if request.method=="POST":
		username=request.form['username']
		password=request.form['password']
		resultSet,data=checkUser(username)
		print("data: ",data)
		if resultSet>0:
			_password=data['password']
			if sha256_crypt.verify(password,_password):
				if True:
					session['username']=username
					session['logged_in']=True
					flash('You are logged in', 'success')
					return redirect(url_for('messages'))
				else:
					error = 'User not found'
					return render_template('login.html',error=error)
		else:
			error = "Username not found"
			return render_template('login.html',error=error)
	return render_template('login.html')


@app.route('/logout')
@is_logged_in
def logout():
	session.clear()
	flash('You are now logged out!', 'success')
	return redirect(url_for("login"))
#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________


#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________

@app.route("/send/<string:user>",methods=["GET","POST"])
def send(user):
	frm=MessagesForm(request.form)
	if request.method=="POST" and frm.validate():
		message=frm.message.data
		addMessage(user,message)
		return redirect(url_for("index"))
	return render_template("add_message.html",form=frm)

@app.route("/about")
def about():
	return render_template("about.html")


@app.route('/msg')
@is_logged_in
def messages():
	user="yasser"
	resultSet,data=getMessages(user)
	if resultSet>0:
		return render_template("messages.html",data=data,user=user)
	else:
		msg = "No Messages found"
		return render_template("messages.html",msg=msg)

#__________________________________________________________________________________________________________
#__________________________________________________________________________________________________________

if __name__ == '__main__' :
	app.run(debug = True, host = '127.0.0.1', port = '8000')
