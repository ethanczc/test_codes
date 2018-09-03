from tkinter import *
import tkinter.messagebox
import time
import threading
import random

root = Tk()
root.title('tkinter threading datalog')
clockLabel = Label(root, text='clock',font=('times',20))
clockLabel.grid(row=0,column=0, padx=5,pady=5,sticky=E)
clock = Label(root, font=('times', 30, 'bold'), bg='green')
clock.grid(row=0,column=1,pady=5, padx=5,sticky=W)
intervalLabel = Label(root, text='Interval (min)', font=('times',20))
intervalLabel.grid(row=1,column=0, padx=5,pady=5,sticky=E)
intervalEntry = Entry(root, font=('times',20),width=4)
intervalEntry.grid(row=1,column=1, padx=5,pady=5,sticky=W)

logListBox = Listbox(root, font=('times',20))
logListBox.grid(row=3,column=0, columnspan=2,pady=5,sticky=W+E)

logState = False

def tick():

    timeNow = time.strftime('%H:%M:%S')
    clock.config(text=timeNow)
    root.after(200, tick)
    
def logData():
    while True:
        if logState == True:
            file = open("log.txt", "a")
            timeNow = time.strftime('%H:%M:%S')
            file.write('{} \n'.format(timeNow))
            file.close()
            intervalSec = float(intervalEntry.get())
            intervalMin = intervalSec * 60
            logListBox.yview(END)
            randomNumber = random.randint(1,100)
            AddToListBox('{}: {}'.format(timeNow,randomNumber))
            time.sleep(intervalMin)
        
def logFunction():
    global logState   
    logState = not logState
    if logState == True:
        buttonLog.config(text='Stop Logging')
        logListBox.insert(END,'Logging Started')
        file = open("log.txt", "a")
        file.write('logging started \n')
        file.close()
    else:
        buttonLog.config(text='Start Logging')
        logListBox.insert(END,'Logging Stop')
        file = open("log.txt", "a")
        file.write('logging stopped \n')
        file.close()
        
def AddToListBox(timeNow):
    logListBox.insert(END,timeNow)
    length = logListBox.size()
    if length > 10:
        logListBox.delete(0)
    
buttonLog = Button(root,text='Start Logging',font=('times',20),command=logFunction)
buttonLog.grid(row=2,column=0,columnspan=2,padx=5,sticky=W+E)

if __name__ == '__main__':
    tick()
    logging = threading.Thread(name='timer1',target=logData, daemon=True)
    logging.start()
    root.mainloop()