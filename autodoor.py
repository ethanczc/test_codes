import RPI.GPIO as GPIO
import paho.mqtt.client as mqtt

pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin,GPIO.OUT)

def TurnOn():
	GPIO.output(pin,True)

def TurnOff():
	GPIO.output(pin,False)

host = 'm16.cloudmqtt.com'
topic = 'autodoor'
port = 11499

def on_connect(client, userdata, flags, rc):
	print ('connected code: ' + str(rc))
	client.subscribe(topic)

def on_message(client, userdata, msg):
	message = str(msg.payload)
	message = message[2:-1]
	if message == '1':
		TurnOn()
	elif message == '0':
		TurnOff()

client = mqtt.Client()
client.username_pw_set(username= 'rgexthtd', password= 'unfoeYhhF3OW')
client.on_connect = on_connect
client.on_message = on_message

client.connect(host, port, 60)
client.loop_forever()