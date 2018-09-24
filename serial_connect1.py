from tkinter import*
import serial
import threading
import time
import os
'''
User can enter serial port number from the GUI instead of editing the source code.
User can then open multiple instances of the source code, but assign the program to
the user's desired com port.
'''
root = Tk()
root.title('serial manual connection')
root.geometry('')

serialPort_Label = Label(root,text='port no.').grid(row=0,column=0)
serialPort_Entry = Entry(root)
serialPort_Entry.grid(row=0,column=1)
serialPort_Entry.insert(END,'/dev/ttyUSB0')

ser = serial.Serial()
ser.baudrate = 9600

def SerialConnect():
	serialAddress = serialPort_Entry.get()
	ser.port = str(serialAddress)
	try:
		ser.open()
	except:
		serialStatus_Display.config(text='failed to connect')
	else:
		serialStatus_Display.config(text=serialAddress)
		serialPort_Entry.config(state='disable')
		serialConnect_Button.config(state='disable')
		checkIncomingSerial_Thread = threading.Thread(target=CheckIncomingSerial,daemon=True)
		checkIncomingSerial_Thread.start()
		t_stop = threading.Event()
		serialStatusCheck_Thread = threading.Thread(target=ContinuousSerialCheck,args=(1,t_stop,serialAddress),daemon=True)
		serialStatusCheck_Thread.start()

serialConnect_Button = Button(root, text='connect',command=SerialConnect)
serialConnect_Button.grid(row=1,column=0,columnspan=2)

serialStatus_Label = Label(root,text='connected port:').grid(row=2,column=0)
serialStatus_Display = Label(root,text='disconnected')
serialStatus_Display.grid(row=2,column=1)

def ContinuousSerialCheck(arg1,stop_event,serialAddress):
	'''
	this function is run by a seperate thread to continuously check on the connection status \
	by opening ls /dev/tty'usb port'. if there is a detected device according to the set address \
	the label displays the connected port number. \
	The thread only runs when the serial connection is established, and thread stops when os stops \
	detecting the specified serial address. The continuous monitoring checks every 3 seconds.
	'''
	while not stop_event.is_set():
		try:
			x=os.system('ls {}'.format(serialAddress))
		except:
			stop_event.set()
		else:
			if x == 0:
				serialStatus_Display.config(text=serialAddress)
			else:
				serialStatus_Display.config(text='disconnected')
		stop_event.wait(timeout=3)

def CheckIncomingSerial():
	print('listening to incoming serial')
	while True:
		try:
			rawData = ser.readline()
			rawData = rawData.decode('utf-8')
			rawData = rawData[:-2]
			rawDataList = rawData.split(' ')
			command = rawDataList[0]
			value = float(rawDataList[1])
		except:
			pass
		else:
			processedData = [command,value]
			CheckData(processedData)
			print(processedData)

def CheckData(processedData):
	pass

def main():
	root.mainloop()

if __name__ == '__main__':
	main()