# everything is a kind of widget in tkinter
# 1st we ctate a thing than display on screen

from tkinter import *

root = Tk()


# create a function to work by button
def myClick():
    myLabel = Label(root, text='Hello  '+ e.get() + '  !!!')
    myLabel.pack()


# creating a Entry widget for InputFild
e = Entry(root, width=50, bg='green',borderwidth=10)
# Shoving it onto the screen
e.pack()
# insert text inside field
e.insert(0, "Name...........")



# creating a Button widget and 
myButton1 = Button(root, text="Enter Your Name", padx=200,pady=10, command=myClick,bg='blue',fg='#fff')
myButton1.pack()


# display over and over by looping
root.mainloop()








