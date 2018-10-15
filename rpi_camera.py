import picamera
import time

camera = picamera.PiCamera()
captureTime = ['10:16:20','12:00:00','17:00:00']
timeNow =''
dateNow = ''

def Capture(dateNow,timeNow):
	camera.start_preview()
	time.sleep(5)
	camera.capture('/home/pi/{}/{}.jpeg'.format(dateNow,timeNow))
	camera.stop_preview()

def main():
	global timeNow, dateNow
	while True:
		timeNow = time.strftime('%H:%M:%S')
		dateNow = time.strftime('%d/%m/%y')
		for thisTime in captureTime:
			if thisTime == timeNow:
				Capture(dateNow,timeNow)
		time.sleep(1)

if __name__ == '__main__':
	main()
