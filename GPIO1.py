from tkinter import*
import time
import RPi.GPIO as GPIO

root= Tk()
root.title('GPIO')
    
GPIO.setmode(GPIO.BCM)
device = 17
GPIO.setup(device,GPIO.OUT)
timeStart = []
timeEnd = []
defaultTimeStart1 = StringVar(root,value='08 : 00 : 00')
defaultTimeEnd1 = StringVar(root,value='08 : 10 : 00')
defaultTimeStart2 = StringVar(root,value='10 : 00 : 00')
defaultTimeEnd2 = StringVar(root,value='10 : 10 : 00')
defaultTimeStart3 = StringVar(root,value='12 : 00 : 00')
defaultTimeEnd3 = StringVar(root,value='12 : 10 : 00')
defaultTimeStart4 = StringVar(root,value='14 : 00 : 00')
defaultTimeEnd4 = StringVar(root,value='14 : 10 : 00')
defaultTimeStart5 = StringVar(root,value='16 : 00 : 00')
defaultTimeEnd5 = StringVar(root,value='16 : 10 : 00')
defaultTimeStart6 = StringVar(root,value='18 : 00 : 00')
defaultTimeEnd6 = StringVar(root,value='18 : 10 : 00')
defaultTimeStart7 = StringVar(root,value='00 : 00 : 00')
defaultTimeEnd7 = StringVar(root,value='0 : 00 : 00')
defaultTimeStart8 = StringVar(root,value='00 : 00 : 00')
defaultTimeEnd8 = StringVar(root,value='00 : 00 : 00')

def TurnOn():
    GPIO.output(device,True)
    deviceStatusDisplay.config(text='ON',fg='green')
    
def TurnOff():
    GPIO.output(device,False)
    deviceStatusDisplay.config(text='OFF',fg='red')
    


def TimeSave():
    global timeStart, timeEnd
    timeStart = []
    timeEnd = []
    timeStart.extend([time1Start.get(),time2Start.get(),time3Start.get(),time4Start.get(),time5Start.get(),time6Start.get(),time7Start.get(),time8Start.get()])
    timeEnd.extend([time1End.get(),time2End.get(),time3End.get(),time4End.get(),time5End.get(),time6End.get(),time7End.get(),time8End.get()])
    
def Tick():
    global timeStart, timeEnd
    timeNow = time.strftime('%H : %M : %S')
    for timeCheck in timeStart:
        if timeNow == timeCheck:
            TurnOn()         
    for timeCheck in timeEnd:
        if timeNow == timeCheck:
            TurnOff()
    clockDisplay.config(text=timeNow)
    clockDisplay.after(1000, Tick)
    
timeStartLabel = Label(root,text='Start Array').grid(row=0,column=0)
timeEndLabel = Label(root,text='End Array').grid(row=0,column=1)

time1Start = Entry(root,textvariable=defaultTimeStart1)
time1Start.grid(row=1,column=0)
time1End = Entry(root,textvariable=defaultTimeEnd1)
time1End.grid(row=1,column=1)

time2Start = Entry(root,textvariable=defaultTimeStart2)
time2Start.grid(row=2,column=0)
time2End = Entry(root,textvariable=defaultTimeEnd2)
time2End.grid(row=2,column=1)

time3Start = Entry(root,textvariable=defaultTimeStart3)
time3Start.grid(row=3,column=0)
time3End = Entry(root,textvariable=defaultTimeEnd3)
time3End.grid(row=3,column=1)

time4Start = Entry(root,textvariable=defaultTimeStart4)
time4Start.grid(row=4,column=0)
time4End = Entry(root,textvariable=defaultTimeEnd4)
time4End.grid(row=4,column=1)

time5Start = Entry(root,textvariable=defaultTimeStart5)
time5Start.grid(row=5,column=0)
time5End = Entry(root,textvariable=defaultTimeEnd5)
time5End.grid(row=5,column=1)

time6Start = Entry(root,textvariable=defaultTimeStart6)
time6Start.grid(row=6,column=0)
time6End = Entry(root,textvariable=defaultTimeEnd6)
time6End.grid(row=6,column=1)

time7Start = Entry(root,textvariable=defaultTimeStart7)
time7Start.grid(row=7,column=0)
time7End = Entry(root,textvariable=defaultTimeEnd7)
time7End.grid(row=7,column=1)

time8Start = Entry(root,textvariable=defaultTimeStart8)
time8Start.grid(row=8,column=0)
time8End = Entry(root,textvariable=defaultTimeEnd8)
time8End.grid(row=8,column=1)

buttonSave = Button(root,text='Save',command=TimeSave).grid(row=9,column=0,columnspan=2)
      
clockDisplay = Label(root, font=('times', 12, 'bold'), bg='white')
clockDisplay.grid(row=10,column=0,columnspan =2)

buttonStart=Button(root,text='Start',command=TurnOn).grid(row=11,column=0)
buttonStop=Button(root,text='Stop',command=TurnOff).grid(row=11,column=1)

deviceStatus = Label(root, text='Status').grid(row=12,column=0)
deviceStatusDisplay = Label(root,font=('times', 12, 'bold'))
deviceStatusDisplay.config(text='OFF',fg='red')
deviceStatusDisplay.grid(row=12,column=1)

Tick()

if __name__ == '__main__':
    root.mainloop()