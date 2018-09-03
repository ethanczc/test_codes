import time
from tkinter import*

root= Tk()

autoNotification=BooleanVar()

def CheckButton1Checked():
    displayLabel.config(text=autoNotification.get())
        
checkbutton1 = Checkbutton(root,text='Auto notifications',variable = autoNotification,command=CheckButton1Checked)
checkbutton1.grid(row=0, column=0)
displayLabel = Label(root,text='')
displayLabel.grid(row=1,column=0)



root.mainloop()