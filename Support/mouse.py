#Import tkinter library
from tkinter import *
from PIL import Image, ImageTk
#Create an instance of tkinter frame or window
window= Tk()
#Setting Fullscreen
width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
#Set the geometry of tkinter frame
window.geometry("%dx%d" % (width, height))
def callback(e):
   x= e.x
   y= e.y
   print("Pointer is currently at %d, %d" %(x,y))
window.bind('<Motion>',callback)
window.mainloop()