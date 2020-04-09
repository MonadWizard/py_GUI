# min (4:16:36)

from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title('Monad Wizard.........')
root.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
root.geometry('400x800')  # window size



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


# create a function to delete a record from Data Base

def delete():
    # create a date base or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor to purfom all operation
    c = conn.cursor()
    
    
    # Delete a record
    c.execute("DELETE from addresses WHERE oid= " + delete_box.get())
    
    delete_box.delete(0, END)
    
    
    # commit change
    conn.commit()
    
    # close connection
    conn.close()




def update():
    # create a date base or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor to purfom all operation
    c = conn.cursor()
     
    record_id = delete_box.get()
    c.execute("""UPDATE addresses SET
              first_name = :first,
              last_name = :last,
              address = :address,
              city = :city,
              state = :state,
              zipcode = :zipcode
              
              WHERE oid = :oid""",
              {
               'first': f_name_editor.get(),
               'last': l_name_editor.get(),
               'address': address_editor.get(),
               'city': city_editor.get(),
               'state': state_editor.get(),
               'zipcode': zipcode_editor.get(),
               
               'oid': record_id
                      
                
                      
                      })


    # commit change
    conn.commit()
    
    # close connection
    conn.close()
    
    # close editor window
    editor.destroy()









# create edit function to update a Record create new window here
def edit():
    global editor
    editor = Tk()
    editor.title('Update Record')
    editor.iconbitmap('D:\\code\\pyGUI\\TKINTER\\mw.ico')
    editor.geometry('400x200')  # window size
    
       
       
    # create a date base or connect to one
    conn = sqlite3.connect('address_book.db')
    
    # create a cursor to purfom all operation
    c = conn.cursor()
   
    
    record_id = delete_box.get()
    # Query the DataBase    
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id) # oid is unique primary key 
    records = c.fetchall()

 
    # create global variable for text box name
    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zipcode_editor




    # create Text Box
    
    f_name_editor = Entry(editor, width=30 )
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10,0))
    
    l_name_editor = Entry(editor, width=30 )
    l_name_editor.grid(row=1, column=1)
    
    address_editor = Entry(editor, width=30 )
    address_editor.grid(row=2, column=1)
    
    city_editor = Entry(editor, width=30 )
    city_editor.grid(row=3, column=1)
    
    state_editor = Entry(editor, width=30 )
    state_editor.grid(row=4, column=1)
    
    zipcode_editor = Entry(editor, width=30 )
    zipcode_editor.grid(row=5, column=1)
    

    
    # create text box Labels
    f_name_label_editor = Label(editor, text="First Name")
    f_name_label_editor.grid(row=0, column=0, pady=(10,0) )
    
    l_name_label_editor = Label(editor, text="Last Name")
    l_name_label_editor.grid(row=1, column=0 )
    
    address_label_editor = Label(editor, text="Address")
    address_label_editor.grid(row=2, column=0 )
    
    city_label_editor = Label(editor, text="City")
    city_label_editor.grid(row=3, column=0 )
    
    state_label_editor = Label(editor, text="State")
    state_label_editor.grid(row=4, column=0 )
    
    zipcode_label_editor = Label(editor, text="Zip Code")
    zipcode_label_editor.grid(row=5, column=0 )
  
    
    
    # Loop through results
    for record in records:
        f_name_editor.insert(0, record[0])
        l_name_editor.insert(0, record[1])
        address_editor.insert(0, record[2])
        city_editor.insert(0, record[3])
        state_editor.insert(0, record[4])
        zipcode_editor.insert(0, record[5])
    


    # Create an Save Button to save edited record
    save_btn = Button(editor, text="Save Records", command=update)
    save_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=135 )
    




    







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
    query_label.grid(row=12, column=0, columnspan=2)
    
    
    
    
    # commit change
    conn.commit()
    
    # close connection
    conn.close()




# create Text Box

f_name = Entry(root, width=30 )
f_name.grid(row=0, column=1, padx=20, pady=(10,0))

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

# create entry to delete item
delete_box = Entry(root, width=30 )
delete_box.grid(row=8, column=1)





# create text box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10,0) )

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

# create a text box label for Delete item
delete_box_label = Label(root, text="Select ID")
delete_box_label.grid(row=8, column=0)



# create submit button
submit_btn = Button(root, text="Add record to Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=115 )


# create a query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, pady=10, padx=10, ipadx=139 )


# Create a Delete Button
delete_btn = Button(root, text="Delete Records", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, pady=10, padx=10, ipadx=138 )

# Create an Update Button
edit_btn = Button(root, text="Update Records", command=edit)
edit_btn.grid(row=10, column=0, columnspan=2, pady=10, padx=10, ipadx=135 )





root.mainloop()

