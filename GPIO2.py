from tkinter import*
import time
import RPi.GPIO as GPIO
import threading

root= Tk()
root.title('FIXED INTERVALS')
root.geometry('300x220')

GPIO.setmode(GPIO.BCM)
device = 17
GPIO.setup(device,GPIO.OUT)
autoMode = False
cycleLength = StringVar(root,value='5')
cycleWait = StringVar(root,value='10')
defaultStartTime = StringVar(root,value='07:00:00')
defaultEndTime = StringVar(root,value='19:00:00')

def TurnOn():
    GPIO.output(device,True)
    deviceStatusDisplay.config(text='ON',fg='green')
    
def TurnOff():
    GPIO.output(device,False)
    deviceStatusDisplay.config(text='OFF',fg='red')
    
def AutoModeToggle():
    global autoMode, cycleLength, cycleWait
    autoMode = not autoMode
    if autoMode == True:
        autoStateDisplay.config(text='AUTO',fg='blue')
        autoButton.config(text='MANUAL')
        buttonStart.config(state='disabled')
        buttonStop.config(state='disabled')
        cycleLength=(float(cycleLengthInput.get())) * 60
        cycleWait=(float(cycleWaitInput.get())) * 60
        
    else:
        autoStateDisplay.config(text='MANUAL',fg='yellow')
        autoButton.config(text='AUTO')
        buttonStart.config(state='normal')
        buttonStop.config(state='normal')
    
def Cycling():
    while True:
        global autoMode, cycleLength, cycleWait

        timeNow = time.strptime(time.strftime('%H:%M:%S'),'%H:%M:%S')
        timeStart = time.strptime(timeStartInput.get(),"%H:%M:%S")
        timeEnd = time.strptime(timeEndInput.get(),"%H:%M:%S")
        if timeNow > timeStart and timeNow < timeEnd:
            withinTimePeriodDisplay.config(text='Yes',fg='green')
            if autoMode == True:
                TurnOn()
                time.sleep(cycleLength)
                TurnOff()
                time.sleep(cycleWait)
            else:
                pass
        else:
            withinTimePeriodDisplay.config(text='No',fg='black')
    
def TimeSave():
    pass
    
def Tick():
    timeNow = time.strftime('%H : %M : %S')
    clockDisplay.config(text=timeNow)
    clockDisplay.after(1000, Tick)
    
clockDisplay = Label(root, font=('times', 16, 'bold'), bg='white')
clockDisplay.grid(row=0,column=0,columnspan =2,padx=5,pady=5)

autoButton = Button(root,text='Auto',command=AutoModeToggle)
autoButton.grid(row=1,column=0)
autoStateDisplay = Label(root)
autoStateDisplay.config(text='MANUAL',fg='yellow')
autoStateDisplay.grid(row=1,column=1)

cycleLengthLabel = Label(root,text='Cycle Length').grid(row=2,column=0)
cycleLengthInput = Entry(root,textvariable=cycleLength)
cycleLengthInput.grid(row=2,column=1)
cycleWaitLabel = Label(root,text='Cycle Wait').grid(row=3,column=0)
cycleWaitInput = Entry(root,textvariable=cycleWait)
cycleWaitInput.grid(row=3,column=1)

timeStartLabel = Label(root,text='From').grid(row=4,column=0)
timeStartInput = Entry(root, textvariable=defaultStartTime)
timeStartInput.grid(row=4,column=1)
timeEndLabel = Label(root,text='To').grid(row=5,column=0)
timeEndInput = Entry(root, textvariable=defaultEndTime)
timeEndInput.grid(row=5,column=1)

withinTimePeriodLabel = Label(root,text='In time period').grid(row=6,column=0)
withinTimePeriodDisplay = Label(root)
withinTimePeriodDisplay.grid(row=6,column=1)

buttonStart=Button(root,text='Start',command=TurnOn)
buttonStart.grid(row=11,column=0)
buttonStop=Button(root,text='Stop',command=TurnOff)
buttonStop.grid(row=11,column=1)

deviceStatus = Label(root, text='Status').grid(row=12,column=0)
deviceStatusDisplay = Label(root,font=('times', 12, 'bold'))
deviceStatusDisplay.config(text='OFF',fg='red')
deviceStatusDisplay.grid(row=12,column=1)

Tick()

def main():
    cyclingThread = threading.Thread(name='cycle',target=Cycling, daemon=True)
    cyclingThread.start()
    root.mainloop()
    
if __name__ == '__main__':
    main()