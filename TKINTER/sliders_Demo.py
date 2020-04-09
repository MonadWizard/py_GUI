from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x400')


# pass a variable to def slide(v) and it work instandly
def slide():
    my_label_h = Label(root, text= horizontal.get()).pack()
    my_label_v = Label(root, text=vertical.get()).pack()
    
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))
    




# create slider 
vertical = Scale(root, from_= 200, to = 500, command=slide)
vertical.pack()


horizontal = Scale(root, from_= 200, to=500, orient=HORIZONTAL, command=slide)
horizontal.pack()

my_label_h = Label(root, text=horizontal.get()).pack()
my_label_v = Label(root, text=vertical.get()).pack()

# pick value of slider position by cutton
my_btn = Button(root, text= "click me", command = slide).pack()





root.mainloop()

