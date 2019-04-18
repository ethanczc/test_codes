from datetime import datetime
import time

while True:
	ms = int(round(time.time() * 1000))
	if ms % 1000 == 0:
		print(time.strftime('%H:%M:%S'))
		time.sleep(0.1)
