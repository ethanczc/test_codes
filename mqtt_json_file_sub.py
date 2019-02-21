import paho.mqtt.client as mqtt
import json
import base64

# Define event callbacks
def on_connect(client, userdata, flags, rc):
    print("rc: " + str(rc))

def on_message(client, obj, msg):
    decodedMessage = (msg.payload.decode("utf-8","ignore"))
    message = json.loads(decodedMessage)
    if message['type'] == 'sensors':
    	print('data received')
    elif message['type'] == 'image':
    	imageString = message['image']
    	encoded = imageString.encode('utf-8')
    	image = base64.b64decode(encoded)
    	with open('newlena.png','wb') as file:
    		file.write(image)
    	print('image received and saved')

def on_publish(client, obj, mid):
    print("mid: " + str(mid))

def on_subscribe(client, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_log(client, obj, level, string):
    print(string)

client = mqtt.Client()
# Assign event callbacks
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

# mqtt broker details
host = '10.42.0.1'
topic = 'ethan'
port = 1883

# Connect
client.connect(host,port,60)

# Start subscribe, with QoS level 0
client.subscribe(topic)

# Continue the network loop, exit when an error occurs
rc = 0
while rc == 0:
    rc = client.loop()
print("rc: " + str(rc))
