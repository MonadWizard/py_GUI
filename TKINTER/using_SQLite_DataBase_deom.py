from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x400')  # window size



# DataBase.........................................................

# create table that just run for 1st time 
'''
c.execute(""" 
          CREATE TABLE addresses (
          first_name text,
          last_name text,
          address text,
          city text,
          state text,
          zipcode integer
          
          )
""")

'''





# Create Submit Function For database
def submit():
    # create a date base or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor to purfom all operation
    c = conn.cursor()
    
    # Insert Into Table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                      'f_name': f_name.get(),
                      'l_name': l_name.get(),
                      'address': address.get(),
                      'city': city.get(),
                      'state': state.get(),
                      'zipcode': zipcode.get(),
                      }
              )
    
    
    
    # commit change
    conn.commit()
    
    # close connection
    conn.close()

 
    # Clear the Text Boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)




def query():
    
    # create a date base or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor to purfom all operation
    c = conn.cursor()
    
    
    # Query the DataBase    
    c.execute("SELECT *, oid FROM addresses") # oid is unique primary key 
    records = c.fetchall()
#    print(records)
    
    # Loop to see all Result
    print_records = ''
    for record in records:
#        print_records += str(record) + "\n"  
        print_records += str(record[6])+ "\t" + "First Name: " + str(record[0])+ "    Last Name: " + str(record[1]) + "\n"

        
    query_label = Label(root, text= print_records)
    query_label.grid(row=8, column=0, columnspan=2)
    
    
    
    
    # commit change
    conn.commit()
    
    # close connection
    conn.close()




# create Text Box

f_name = Entry(root, width=30 )
f_name.grid(row=0, column=1, padx=20)

l_name = Entry(root, width=30 )
l_name.grid(row=1, column=1)

address = Entry(root, width=30 )
address.grid(row=2, column=1)

city = Entry(root, width=30 )
city.grid(row=3, column=1)

state = Entry(root, width=30 )
state.grid(row=4, column=1)

zipcode = Entry(root, width=30 )
zipcode.grid(row=5, column=1)




# create text box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0 )

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0 )

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0 )

city_label = Label(root, text="City")
city_label.grid(row=3, column=0 )

state_label = Label(root, text="State")
state_label.grid(row=4, column=0 )

zipcode_label = Label(root, text="Zip Code")
zipcode_label.grid(row=5, column=0 )




# create submit button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100 )


# create a query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=100 )







root.mainloop()

