from tkinter import *
import sqlite3

root = Tk()
root.title('Address Book Application')
root.iconbitmap('calculator.ico')
root.geometry('400x300')

def submit():
	#Create a database or connect to one
	conn = sqlite3.connect('database.db')
	#Create a cursor to execute sql quries
	c = conn.cursor()
	# Create table
	# c.execute('''CREATE TABLE addresses(
	# 	first_name text,
	# 	last_name text,
	# 	address text,
	# 	city text,
	# 	state text,
	# 	zipcode integer
	# )''')
	# insert values 
	c.execute('INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)',
			{
				'f_name': f_name.get(),
				'l_name': l_name.get(),
				'address': address.get(),
				'city': city.get(),
				'state': state.get(),
				'zipcode': zipcode.get()
			}
		)
	#Commit Changes
	conn.commit()
	#Close Connection
	conn.close()
	#delete existing entries
	f_name.delete(0,END)
	l_name.delete(0,END)
	address.delete(0,END)
	city.delete(0,END)
	state.delete(0,END)
	zipcode.delete(0,END)

def show():
	columns=['First',' Last', 'Street', 'City','State','Zip']
	top=Toplevel()
	top.geometry('450x400')

	for i in range(6): 
		cn = Label(top, text=str(columns[i]), font=('Arial',16,'bold'))
		cn.grid(row=0, column=i) 

	conn = sqlite3.connect('database.db')
	c =conn.cursor()
	c.execute('SELECT * FROM addresses')
	records = c.fetchall()

	for i in range(len(records)): 
            for j in range(len(records[0])): 
       
                e = Label(top, text=str(records[i][j])) 
                e.grid(row=i+1, column=j) 
 
	print(records)
	conn.commit()
	conn.close()





# gui arrangement
title = Label(root, text='Address Book', font=('Arial',20,'bold'))
title.grid(row=0, column=0, columnspan=2)

f_name = Entry(root, width=30)
f_name.grid(row=1, column=1)
l_name = Entry(root, width=30)
l_name.grid(row=2, column=1)
address = Entry(root, width=30)
address.grid(row=3, column=1)
city = Entry(root, width=30)
city.grid(row=4, column=1)
state = Entry(root, width=30)
state.grid(row=5, column=1)
zipcode = Entry(root, width=30)
zipcode.grid(row=6, column=1)

f_nameL = Label(root, text='First name')
f_nameL.grid(row=1, column=0)
l_nameL = Label(root, text='Last name')
l_nameL.grid(row=2, column=0)
addressL = Label(root, text='Address')
addressL.grid(row=3, column=0)
cityL = Label(root, text='City')
cityL.grid(row=4, column=0)
stateL = Label(root, text='State')
stateL.grid(row=5, column=0)
zipcodeL = Label(root, text='Zipcode')
zipcodeL.grid(row=6, column=0)




submit_btn = Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=7,column=0, columnspan=2, padx=10, pady=5, ipadx=100)

show_btn = Button(root, text='Show All Record', command=show)
show_btn.grid(row=8,column=0, columnspan=2, padx=10, ipadx=124)




root.mainloop()