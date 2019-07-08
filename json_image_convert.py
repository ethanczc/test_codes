import json
import sys
import base64

with open('lena.png','rb') as file:
	byteContent = file.read()
base64Bytes = base64.b64encode(byteContent)
base64String = base64Bytes.decode('utf-8')
rawData = {
	'image' : base64String,
	'type': 'image'
}

data = json.dumps(rawData)

received = json.loads(data)

imageString = received['image']
encoded = imageString.encode('utf-8')
image = base64.b64decode(encoded)

with open('newlena.png','wb') as file:
	file.write(image)
