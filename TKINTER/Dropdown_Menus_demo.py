from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x400')  # window size




def pick():
    lable = Label(root, text=clicked.get()).pack()


# Drop Down Boxes
clicked = StringVar()
clicked.set("Friday") # as default item

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednestday", "Friday","Saturday", "sunday")
drop.pack()


myButton = Button(root, text="Pick date", command= pick).pack()







# using List.................
option = [
        "Monday",
        "Tuesday",
        "Wednestday",
        "Friday",
        "Saturday", 
        "sunday"
        ]



def pickL():
    lable = Label(root, text=clickedL.get()).pack()


# Drop Down Boxes
clickedL = StringVar()
clickedL.set(option[1]) # as default item

drop = OptionMenu(root, clickedL, *option)
drop.pack()


myButtonL = Button(root, text="Pick date List", command= pickL).pack()
















root.mainloop()

