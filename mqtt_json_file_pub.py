import paho.mqtt.publish as publish
import json
import sys
import datetime
import base64

# mqtt broker details
host = '10.42.0.1'
topic = 'ethan'
port = 1883

# time 
now = datetime.datetime.now()
datetime = '%s/%s/%s %s:%s:%s' \
%(now.year,now.month,now.day,now.hour,now.minute,now.second)

# image encoding
image = 'lena.png'
with open(image,'rb') as file:
	fileContent = file.read()
base64Bytes = base64.b64encode(fileContent)
base64String = base64Bytes.decode('utf-8')

sensorsMessage = {
	'type' : 'sensors',
	'datetime' : datetime,
	't' : 28.15
}

imageMessage = {
	'type' : 'image',
	'datetime' : datetime,
	'image' : base64String
}

def Publish(jsonMessage):
	message = json.dumps(jsonMessage,sort_keys=True)
	publish.single(topic,payload=message,hostname=host,port=port)
	size = sys.getsizeof(message)
	print('file has been sent. Payload: ' + str(size) + ' bytes')

def main():
	Publish(imageMessage)

if __name__ == '__main__':
	main()
