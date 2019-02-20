import pymysql


#connect to db
def connect_db():
	try:
		connection = pymysql.connect(
									host='localhost',
									user='root',
									password='',
									db='sarahah',
									charset = 'utf8',
									cursorclass=pymysql.cursors.DictCursor
									)
		db = connection.cursor()
		return connection,db
	except:
		print("Connection To DataBase Failed !")
		return (0,0)

#insert data into database
def insertData(query,values):
	try:
		connection,db = connect_db()	
		db.execute(query,values)
		connection.commit()
		db.close()
		return 1
	except:
		return 0

#get all records from database
def getAllData(query,values):
	connection,db = connect_db()
	resultSet = db.execute(query,values)
	data = db.fetchall()
	connection.commit()
	db.close()
	return resultSet,data

#get one record from database
def getOneData(query,values):
	connection,db = connect_db()
	resultSet = db.execute(query,values)
	data = db.fetchone()
	connection.commit()
	db.close()
	return resultSet,data



