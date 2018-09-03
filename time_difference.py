import time
from tkinter import*
import threading

root= Tk()

def ExpiryThread():
    while True:
        t2 = time.time()
        print(int(t2))
        if t2 - t1 >= interval:
            print('done')
            break
        time.sleep(1)

timeExpiryThread = threading.Thread(target=ExpiryThread, daemon=True)

def Send():
    timeExpiryThread.start()
    timeExpiryThread.join()
    t1 = time.time()
        
eventButton = Button(root,text='send',command=Send)
eventButton.grid(row=0,column=0)

interval = 5
t1 = time.time()

root.mainloop()










