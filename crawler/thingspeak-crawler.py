from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import sqlite3
from sqlite3 import Error
import os

api_key = INSERT YOUR KEY HERE

base_url = 'https://api.thingspeak.com/channels/'
query = '1297494/feeds.json?api_key='+api_key

session = Session()

try:
  response = session.get(base_url+query)
  results = json.loads(response.text)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

channel_name = results['channel']['name']
sensor_name = results['channel']['field1']
sensor_description = results['channel']['description']
sensor_unit = "BPM"
sensor_readings = []
reading_times = []

for item in results['feeds']:
  sensor_readings.append(item['field1'])
  reading_times.append(item['created_at'])

database = r'C:\Users\Gustavo\Documents\Graduação\Engenharia Mecatrônica\Optativas\Sistemas Distribuídos\FLASK-API\db\dbsqlite.db'

try:
  conn = sqlite3.connect(database)
except(ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

for index, sensor_reading in enumerate(sensor_readings):
  sql = ''' INSERT INTO sensor_readings (channel_name,sensor_name,sensor_description,sensor_unit,sensor_reading,reading_time)
          VALUES(?,?,?,?,?,?) '''
  sensor_reading = (channel_name,sensor_name,sensor_description,sensor_unit,sensor_reading,reading_times[index]);
  cur = conn.cursor()
  cur.execute(sql, sensor_reading)
  conn.commit()
conn.close()