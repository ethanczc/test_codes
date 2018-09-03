from tkinter import *
import time

class MainFrame(object):
    def __init__(self,master):
        self.master=master
        master.title('hello world')
        master.geometry('800x400')
        master.resizable(width=False,height=False)
        
        self.leftFrame = Frame(master, width=400,height=200, highlightbackground='blue',highlightthickness=1)
        self.leftFrame.grid(row=0,column=0)
        self.rightFrame = Frame(master, width=400, height=200, highlightbackground='blue',highlightthickness=1)
        self.rightFrame.grid(row=0,column=1)
        self.bottomFrame = Frame(master, width=800, height=200,bg='white',borderwidth=1)
        self.bottomFrame.grid(row=1,column=0,columnspan=2)
##        self.bottomCanvas = Canvas(self.bottomFrame, width=800, height=200,bg='white')
##        self.bottomCanvas.pack()

        self.clockDisplay = Label(self.leftFrame, font=('times', 20, 'bold'), bg='green')
        self.clockDisplay.grid(row=0, padx=10,pady=10)
        self.clockLabel = Label(self.leftFrame, text = 'clock')
        self.clockLabel.grid(row=1)
        self.tick()
        
        self.label = Label(self.rightFrame, text = 'hello', font=('times',30))
        self.label.grid(row=0)
        self.label2 = Label(self.rightFrame, text = 'hello')
        self.label2.grid(row=1)
        
    def tick(self):
        timeNow = time.strftime('%H:%M:%S')
        self.clockDisplay.config(text=timeNow)
        self.clockDisplay.after(200, self.tick)
    
def main():
    root = Tk()
    mainFrame = MainFrame(root)
    root.mainloop()
    
if __name__ == '__main__':
    main()