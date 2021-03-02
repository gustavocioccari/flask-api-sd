from flask import Flask
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
from requests import Request, Session
import sqlite3
from sqlite3 import Error
import json
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
