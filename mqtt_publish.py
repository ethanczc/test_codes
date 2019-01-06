# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single('topic1', 'Hello', hostname='10.42.0.137')
print("Done")
