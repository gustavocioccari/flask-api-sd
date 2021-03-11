from flask import Flask
from flask import request
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session, Response
import sqlite3
from sqlite3 import Error
import json
from datetime import datetime
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
		form = request.get_json(force=True) 

		params = (form['channel_name'],
					form['sensor_name'],
					form['sensor_description'],
					form['sensor_unit'],
					form['sensor_reading'],
					datetime.now())
		print(params)
		cur = conn.cursor()
		cur.execute(query,params)
		data = cur.fetchall() 
		conn.commit()
		conn.close()
		return form
	except(ConnectionError, Timeout, TooManyRedirects) as e:
		print(e)

@app.route('/reading/<id>',methods = ['PATCH','DELETE','GET'])
def change_data(id): #Update, delete data from data base
	if request.method == 'GET':
		try:
			conn = sqlite3.connect(database)
			query ='''select * from sensor_readings where id=?'''
			params = (id,)
			cur = conn.cursor()
			cur.execute(query,params)
			data = cur.fetchall() 
			conn.commit()
			conn.close()
			return json.dumps(data)
		except(ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
	elif request.method == 'DELETE':
		try:
			conn = sqlite3.connect(database)
			query ='''delete from sensor_readings where id=?'''
			params = (id,)
			cur = conn.cursor()
			cur.execute(query,params)
			data = cur.fetchall() 
			conn.commit()
			conn.close()
			return 'deleted'
		except(ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)
	else:
		try:
			conn = sqlite3.connect(database)
			query ='''update sensor_readings
								set channel_name=?,
									sensor_name=?,
									sensor_description=?,
									sensor_unit=?,
									sensor_reading=?,
									reading_time=? where id=?
							'''
			form = request.get_json(force=True) 

			params = (form['channel_name'],
						form['sensor_name'],
						form['sensor_description'],
						form['sensor_unit'],
						form['sensor_reading'],
						datetime.now(),
						id)
			print(params)
			cur = conn.cursor()
			cur.execute(query,params)
			data = cur.fetchall() 
			conn.commit()
			conn.close()
			return form
		except(ConnectionError, Timeout, TooManyRedirects) as e:
			print(e)