# min 3:09


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x400')  # window size



def show():
    myLable = Label(root,text=var.get()).pack()





# for pick value
var = StringVar()

# create check box
c = Checkbutton(root, text= "Check this box, I dare you!", variable=var, onvalue="Rakib",offvalue="Rasid")
c.deselect()
c.pack()


myButton = Button(root, text="Show Selection", command=show).pack()







root.mainloop()

