from tkinter import *

root = Tk()
root.title("Simpl Calculator")  #title




# button action methods are


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    f_num = float(first_number)
    e.delete(0, END)
 
    
def button_equ():
    second_number = e.get()
    e.delete(0, END)
    e.insert(0, f_num + float(second_number))


# entry Field
e = Entry(root, width=87, bg='#e8f5e9',borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=3, pady=10)


# define button
button_1 = Button(root, text="1", padx=54,pady=20, command=lambda: button_click(1),bg='#bbdefb',fg='black')
button_2 = Button(root, text="2", padx=50,pady=20, command=lambda: button_click(2),bg='#b3e5fc',fg='black')
button_3 = Button(root, text="3", padx=50,pady=20, command=lambda: button_click(3),bg='#b2ebf2',fg='black')
button_4 = Button(root, text="4", padx=54,pady=20, command=lambda: button_click(4),bg='#bbdefb',fg='black')
button_5 = Button(root, text="5", padx=50,pady=20, command=lambda: button_click(5),bg='#b3e5fc',fg='black')
button_6 = Button(root, text="6", padx=50,pady=20, command=lambda: button_click(6),bg='#b2ebf2',fg='black')
button_7 = Button(root, text="7", padx=54,pady=20, command=lambda: button_click(7),bg='#bbdefb',fg='black')
button_8 = Button(root, text="8", padx=50,pady=20, command=lambda: button_click(8),bg='#b3e5fc',fg='black')
button_9 = Button(root, text="9", padx=50,pady=20, command=lambda: button_click(9),bg='#b2ebf2',fg='black')
button_0 = Button(root, text="0", padx=50,pady=20, command=lambda: button_click(0),bg='#b3e5fc',fg='black')
button_d = Button(root, text=".", padx=52,pady=20, command=lambda: button_click('.'),bg='#e6ffff',fg='black')

button_add = Button(root, text="+", padx=52,pady=20, command= button_add ,bg='#ffcdd2',fg='black')
button_sub = Button(root, text="-", padx=53,pady=20, command=lambda: button_click('-'),bg='#f8bbd0',fg='black')
button_div = Button(root, text="x", padx=53,pady=20, command=lambda: button_click('*'),bg='#e1bee7',fg='black')
button_mul = Button(root, text="/", padx=53,pady=20, command=lambda: button_click('/'),bg='#d1c4e9',fg='black')
button_equ = Button(root, text="=", padx=53,pady=20, command=button_equ,bg='#718792',fg='#fffde7')

                    
button_clr = Button(root, text="c", padx=54,pady=20, command=button_clear,bg='#FCE4EC',fg='black')
button_per = Button(root, text="%", padx=48,pady=20, command=lambda: button_click('%'),bg='#f3e5f5',fg='black')
button_pow = Button(root, text="^", padx=49,pady=20, command=lambda: button_click('^'),bg='#ede7f6',fg='black')
button_fac = Button(root, text="!", padx=54,pady=20, command=lambda: button_click('!'),bg='#e8eaf6',fg='black')

                  
                  
                  
                
# put the button on the screen

button_clr.grid(row=1 , column=0, columnspan=1 )
button_per.grid(row=1 , column=1, columnspan=1  )
button_pow.grid(row=1 , column=2, columnspan=1  )
button_fac.grid(row=1 , column=3, columnspan=1  )
                    

                    
button_1.grid(row=4 , column=0 )
button_2.grid(row=4 , column=1 )
button_3.grid(row=4 , column=2 )

button_4.grid(row=3 , column=0 )
button_5.grid(row=3 , column=1 )
button_6.grid(row=3 , column=2 )

button_7.grid(row=2 , column=0 )
button_8.grid(row=2 , column=1 )
button_9.grid(row=2 , column=2 )

button_0.grid(row=5 , column=1 )
button_d.grid(row=5 , column=2 )
button_equ.grid(row=5 , column=0 )

button_add.grid(row=5 , column=3 )
button_sub.grid(row=4 , column=3 )
button_div.grid(row=3 , column=3 )
button_mul.grid(row=2 , column=3 )








# display over and over by looping
root.mainloop()








