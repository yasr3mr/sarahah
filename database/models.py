from pymysql import escape_string as clean

from passlib.hash import sha256_crypt

from .db import connect_db,insertData,getAllData,getOneData


#add user
def addUser(name,username,email,password):

	#clean fields
	c_name = clean(name)
	c_username = clean(username)
	c_email = clean(email)
	c_password = sha256_crypt.hash(clean(password))#hash password
	
	#execute query
	d = insertData("insert into users (name,username,email,password) values(%s,%s,%s,%s)",(c_name,c_username,c_email,c_password))
	print (d)
#check username
def checkUser(username):
	#clean
	c_username = clean(username)
	#query
	query = "select * from users where username=%s"
	return getOneData(query,[c_username])

#add message
def addMessage(user,message):
	c_user = clean(user)
	c_message = clean(message)
	
	#query
	query = "insert into messages(user,message) values(%s,%s)"
	#execute query
	return insertData(query,(c_user,c_message))

#get messages for user		
def getMessages(username):
	#clean
	c_user=clean(username)
	#query
	query = "select  * from  messages where user=%s"
	return getAllData(query,[c_user])
	


