from tkinter import *
import tkinter
from tkinter.tix import COLUMN
master = Tk()
master.title("Bill")
master.geometry("400x600")
Label(master, text='Name').grid(row=0, column = 0)
Label(master, text='Number').grid(row=0, column=2)
Label(master, text='Item Name').grid(row=3, column=1)
e1 = Entry(master)
e2 = Entry(master)
e1.grid(row=0, column=3)
e2.grid(row=0, column=1)
B=tkinter.Button(row=2,column=1)
mainloop()