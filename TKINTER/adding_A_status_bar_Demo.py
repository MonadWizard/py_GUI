# min 1:49

from tkinter import *
# python image library(PIL)
from PIL import ImageTk, Image 

root = Tk()
root.title('Images Demo')

# add a icon
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')



# display an Image
my_img_1 = ImageTk.PhotoImage(Image.open("C:\\Users\\CareLess\\Pictures\\pic\\akfa.jpg"))
my_img_2 = ImageTk.PhotoImage(Image.open("C:\\Users\\CareLess\\Pictures\\pic\\MytwoBrothers.jpg"))
my_img_3 = ImageTk.PhotoImage(Image.open("C:\\Users\\CareLess\\Pictures\\pic\\akfa.jpg"))
my_img_4 = ImageTk.PhotoImage(Image.open("C:\\Users\\CareLess\\Pictures\\pic\\MytwoBrothers.jpg"))
my_img_5 = ImageTk.PhotoImage(Image.open("C:\\Users\\CareLess\\Pictures\\pic\\akfa.jpg"))



image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]










my_label = Label(image=my_img_1)
my_label.grid(row=0, column=0, columnspan=3)




def forward(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<<", command=lambda: back(image_number-1))
   
    if image_number == 5:
        button_forward = Button(root, text=">>>", state=DISABLED)
    
    
    
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)
    
    
    
    
    # crate a statud bar
    status = Label(root, text='Image '+ str(image_number) + 'of ' + str(len(image_list)),
                    bd=1, relief=SUNKEN, bg="red", anchor=W)
        
    #define status bar to display
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # sticky make autofill, W=west, E=east




    


def back(image_number):
    global my_label
    global button_forward
    global button_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[image_number-1])
    button_forward = Button(root, text=">>>",command=lambda: forward(image_number+1))
    button_back = Button(root, text="<<<", command=lambda: back(image_number-1))
    
    if image_number == 1:
        button_back = Button(root, text="<<<", state=DISABLED)
    
    
    
   
    my_label.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0)
    button_forward.grid(row=1, column=1)
    
    
       # crate a statud bar
    status = Label(root, text='Image '+ str(image_number) + 'of ' + str(len(image_list)),
                    bd=1, relief=SUNKEN, bg="red", anchor=W)
        
    #define status bar to display
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)  # sticky make autofill, W=west, E=east





button_back = Button(root, text="<<<", command= back, state=DISABLED)
button_forward = Button(root, text=">>>", command= lambda: forward(2))

button_back.grid(row=1, column=0)
button_forward.grid(row=1, column=1, pady=10)






root.mainloop()


