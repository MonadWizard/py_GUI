from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Radio Demo.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')

# pick variable
r= IntVar()

def clicked(value):
    myLable = Label(root, text=value).pack()

# create radio button
Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 3', variable=r, value=3, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 4', variable=r, value=4, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 5', variable=r, value=5, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 6', variable=r, value=6, command=lambda: clicked(r.get())).pack()

# get data to lable
myLable = Label(root, text=r.get()).pack()
myButton = Button(root, text="Click me!", command=lambda: clicked(r.get())).pack()







# using loop.............................

MODES = [
        ("Pepperoni", "Pepperoni"),
        ("cheese", "cheese"),
        ("Mushroom", "Mushroom"),
        ("Onion", "Onion"),
        ("Meat", "Meat"), 
        ]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

def clicked_Pizza(value):
    myLable = Label(root, text=value).pack()

    
# get data to lable
#myLable = Label(root, text=r.get()).pack()

# display data by button
myButton = Button(root, text="Click me!", command=lambda: clicked_Pizza(pizza.get())).pack()









mainloop()


