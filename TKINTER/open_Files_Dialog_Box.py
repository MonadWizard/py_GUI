from tkinter import *
from PIL import ImageTk, Image

from tkinter import filedialog

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x400')



my_btn = Button(root, text= "Open File", command=open).pack()

def open():
    global my_image
    
    #open dialouge box for take specific path in GUI 
    root.filename = filedialog.askopenfilename(initialdir='C:\\Users\\CareLess\\Pictures\\pic',
                                           title="Select a file", 
                                           filetypes=(("png files", "*.png"),("all files", "*.*")))
    # see what return with filename (return path)
    my_label = Label(root, text=root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_image).pack()

    




root.mainloop()

