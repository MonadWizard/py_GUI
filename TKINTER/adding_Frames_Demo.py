from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to create Frames')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')


# creating a frame
frame = LabelFrame(root, text="This is my Frame....", padx=10, pady=50, bg='red')  # inside padding
frame.pack(padx=50, pady=10)  # outside padding


b = Button(frame, text="Don't click here").grid(row=0,column=0)
#b.grid()
b2 = Button(frame, text="2nd Button").grid(row=1,column=1)




root.mainloop()