from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')


"""
# create a demo window
top = Toplevel()
top.title('My second Window')

lbl = Label(top, text= "Hello world...!").pack()

# display an Image
my_img = ImageTk.PhotoImage(Image.open("r.png"))
my_lable = Label(top, image=my_img).pack()

"""

# control window using button
btn = Button(root, text="Open Second Window.", command= open ).pack()


def open():
    global my_img
    # create a demo window
    top = Toplevel()
    top.title('My second Window')
    
    lbl = Label(top, text= "Monad Wizard... ;)").pack()
    
    # display an Image
    my_img = ImageTk.PhotoImage(Image.open("r.png"))
    my_lable = Label(top, image=my_img).pack()
    Button(top, text='close Window', command=top.destroy).pack()








mainloop()

