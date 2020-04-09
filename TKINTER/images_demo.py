from tkinter import *
# python image library(PIL)
from PIL import ImageTk, Image 

root = Tk()
root.title('Images Demo')

# add a icon
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')



# display an Image
my_img = ImageTk.PhotoImage(Image.open("r.png"))
my_lable = Label(image=my_img)
my_lable.pack()










root.mainloop()