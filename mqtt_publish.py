# MQTT Publish Demo
# Publish two messages, to two different topics

import paho.mqtt.publish as publish

publish.single("esp-com", "Hello", hostname="192.168.0.114")
publish.single("esp-com", "World!", hostname="192.168.0.114")
print("Done")