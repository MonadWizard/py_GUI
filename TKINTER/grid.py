# everything is a kind of widget in tkinter
# 1st we ctate a thing than display on screen

from tkinter import *

root = Tk()

# add a icon
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')


# creating a Label widget and  # Shoving it onto the screen
myLabel1 = Label(root, text="Hello World!").grid(row=0, column=0)
myLabel2 = Label(root, text="My name is Rakib Hasan").grid(row=1, column=0)

# Shoving it onto the screen
#myLabel1.grid(row=0, column=0)
#myLabel2.grid(row=1, column=0)


# display over and over by looping
root.mainloop()








