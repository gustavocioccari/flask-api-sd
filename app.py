from flask import Flask
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
import sqlite3
from sqlite3 import Error
import json
from datetime import date
app = Flask(__name__)
database = 'db\dbsqlite.db'

@app.route('/')
def get_all_data():
	try:
		conn = sqlite3.connect(database)
		query ='''select * from sensor_readings'''
		cur = conn.cursor()
		cur.execute(query)
		data = cur.fetchall() 
		conn.commit()
		conn.close()
		return json.dumps(data)
	except(ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)

@app.route('/sensor')
def get_sensor_data():
	try:
		conn = sqlite3.connect(database)
		query ='''select sensor_reading,sensor_unit from sensor_readings'''
		cur = conn.cursor()
		cur.execute(query)
		data = cur.fetchall() 
		conn.commit()
		conn.close()
		return json.dumps(data)
	except(ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)

@app.route('/reading',methods = ['POST'])
def control_data(): #Read, Create data from data base
	try:
		conn = sqlite3.connect(database)
		query ='''insert into sensor_readings (
								channel_name,
								sensor_name,
								sensor_description,
								sensor_unit,
								sensor_reading,
								reading_time)
					values(?,?,?,?,?,?)			
								'''
		form = request.form
		params = (form['channel_name'],
					form['sensor_name'],
					form['sensor_description'],
					form['sensor_unit'],
					form['sensor_reading'],
					today = date.today())
		cur = conn.cursor()
		cur.execute(query,params)
		data = cur.fetchall() 
		conn.commit()
		conn.close()
		return json.dumps(data)
	except(ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)


@app.route('/reading/<id>',methods = ['PATCH','DELETE','GET'])
def change_data(): #Update, delete data from data base
   else:
   		try:
			conn = sqlite3.connect(database)
			query ='''select sensor_reading,sensor_unit from sensor_readings'''
			cur = conn.cursor()
			cur.execute(query)
			data = cur.fetchall() 
			conn.commit()
			conn.close()
			return json.dumps(data)
		except(ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
    	user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user)