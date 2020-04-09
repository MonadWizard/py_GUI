# everything is a kind of widget in tkinter
# 1st we ctate a thing than display on screen

from tkinter import *

root = Tk()


# create a function to work by button
def myClick():
    myLabel = Label(root, text="Look! I clicked a button!!")
    myLabel.pack()





# creating a Button widget and 
myButton1 = Button(root, text="click Me", padx=200,pady=10, command=myClick,bg='blue',fg='#fff')
myButton2 = Button(root, text="My name is Rakib Hasan", state=DISABLED)

# Shoving it onto the screen
myButton1.pack()
myButton2.pack()



"""

# create an exit button
button_quit = Button(root, text="EXIT", command=root.quit)
button_quit.pack()

"""



# display over and over by looping
root.mainloop()








