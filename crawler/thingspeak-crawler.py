from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from datetime import datetime
import os

api_key = 'V8N5Q53BS4XRUQW7'
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
sensor_reading = []
reading_times = []

for item in results['feeds']:
  sensor_reading.append(item['field1'])
  reading_times.append(item['created_at'])

print(channel_name)
print(sensor_name)
print(sensor_description)
print(sensor_unit)
print("Leituras do sensor: ")
print(sensor_reading)
print("Hora das leituras: ")
print(reading_times)