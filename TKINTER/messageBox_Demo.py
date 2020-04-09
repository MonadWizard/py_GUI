from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')


#showinfo, showwarning, showerror, askquestion, askokcancel, askyesno, askyesnocancel, askretrycancel
"""
    showinfoo = messagebox.showinfo("popup title!", "popup message showinfo...!")
    showwarningg = messagebox.showwarning("popup title!", "popup message showwarning...!")
    showerrorr = messagebox.showerror("popup title!", "popup message showerror...!")
    askquestionn = messagebox.askquestion("popup title!", "popup message askquestion...!")
    askokcancell = messagebox.askokcancel("popup title!", "popup message askokcancel...!")
    askyesnoo = messagebox.askyesno("popup title!", "popup message askyesno...!")
    askyesnocancell = messagebox.askyesnocancel("popup title!", "popup message askyesnocancel...!")
    askretrycancell = messagebox.askretrycancel("popup title!", "popup message askretrycancel...!")

"""

def popup():
    askyesnoo = messagebox.askyesno("popup title!", "popup message askyesno...!")

    Label(root, text=askyesnoo).pack()
    if askyesnoo == 1:
        messagebox.showinfo("true", "Rakib Hasan")
    else:
        messagebox.showerror("Fake", "monad Wizard...!")


        
    


Button(root, text="Popup", command=popup).pack()





mainloop()

