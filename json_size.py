import json
import time
import sys

jsonMessage = {
	'node' : 1,
	'time' : time.strftime('%H:%M:%S'),
	'data' : 2,
	}

message = json.dumps(jsonMessage)
print (message)
size = sys.getsizeof(message)
print ('size of payload: ' + str(size) + ' bytes.')