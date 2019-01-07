import paho.mqtt.publish as publish
import time
import json

host = '10.42.0.137'
commandTopic = 'RACK1'
jsonMessage = {
	'state' : 'auto',
	'currentStage' :'3',
	'daysPassed' : '20'
	}

def PublishJsonMessage():
	formattedJson = json.dumps(jsonMessage)
	publish.single(commandTopic, formattedJson, hostname=host)

PublishJsonMessage()
