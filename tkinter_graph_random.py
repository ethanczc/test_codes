import matplotlib
matplotlib.use('TkAgg')
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
##import tkinter as Tk
from tkinter import*
import tkinter.ttk as ttk
import datetime
import time
import threading
import random

root = Tk()

clockLabel = Label(root, text='clock',font=('times',20))
clockLabel.grid(row=0,column=0, padx=5,pady=5)
clock = Label(root, font=('times', 30, 'bold'), bg='white')
clock.grid(row=0,column=1,pady=5, padx=5)

figure = Figure(figsize=(6,4), dpi=100)


canvas = FigureCanvasTkAgg(figure,master=root)
canvas.show()
canvas.get_tk_widget().grid(row=1,column=0,columnspan=2)

xValues = []
yValues = []

def DisplayTime():
    while True:
        timeNow = time.strftime('%H: %M: %S')
        clock.config(text=timeNow)
        time.sleep(1)
        
def PlotGraph():
    global xValues, yValues
    while True:
        graph = figure.add_subplot(111)
        timeNow = datetime.datetime.now()
        xValues.append(timeNow)
        randomValue = random.randint(0,20)
        yValues.append(randomValue)
        graph.plot(xValues,yValues)
        canvas.draw()
        print(xValues)
        time.sleep(3)
        
        if len(xValues)==5:
            figure.clf()
            xValues=[]
            yValues=[]

if __name__ == '__main__': 
    showTime = threading.Thread(name='showTime', target=DisplayTime, daemon=True)
    showTime.start()
    plotter = threading.Thread(target=PlotGraph,daemon=True)
    plotter.start()
    root.mainloop()
    