from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt

root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x200')  # window size

def graph():
    
    house_prices = np.random(200000, 25000, 5000)
    plt.hist(house_prices, 50)
    plt.show()
    
my_button = Button(root, text="Graph It!", command=graph)
my_button.pack()



root.mainloop()

