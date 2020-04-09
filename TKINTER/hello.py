# everything is a kind of widget in tkinter

from tkinter import *

root = Tk()

# add a icon
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')


# creating a Label widget
myLabel = Label(root, text="Hello World!")

# Shoving it onto the screen
myLabel.pack()

# display over and over by looping
root.mainloop()








