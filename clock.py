from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")
root.geometry('390x150+0+0')

def time():
    string = strftime('%H:%M:%S %p')
    label.configure(text=string,background = 'black')
    label.after(1000,time)

label = Label(root,font= 'bold 12',background = 'black',foreground = 'cyan')
label.pack(anchor='center')

time()
mainloop()