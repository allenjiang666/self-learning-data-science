from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()
root.title('Address Book Application')
root.iconbitmap('calculator.ico')
root.geometry('400x300')
root.resizable(False,False)

def submit():
	#Create a database or connect to one
	conn = sqlite3.connect('database.db')
	#Create a cursor to execute sql quries
	c = conn.cursor()

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

def delete():
	# query from db
	conn = sqlite3.connect('database.db')
	c =conn.cursor()
	c.execute('DELETE FROM addresses WHERE oid = (:oid)',{'oid':Id.get()})
	records = c.fetchall()
	conn.commit()
	conn.close()


def show():
	global Id
	columns=['Id','First',' Last', 'Street', 'City','State','Zip']
	top=Toplevel()
	top.geometry('570x400')
	top.resizable(False,False)

	tv = ttk.Treeview(top, columns=(0,1,2,3,4,5,6), show='headings', height='5')
	tv.grid(row=0, column=0, columnspan=3,padx=10)
	
	# change columns width
	for i in range(6):
		tv.column(i, width=70)
	# set the street column a bit wider
	tv.column(3, width=170)
	tv.column(0, width=20)
	tv.column(4, width=90)
	tv.column(6, width=60)

	# change column names
	tv.heading(0, text='ID')
	tv.heading(1, text='First name')
	tv.heading(2, text='Last name')
	tv.heading(3, text='Street')
	tv.heading(4, text='City')
	tv.heading(5, text='State')
	tv.heading(6, text='Zipcode')


	# query from db
	conn = sqlite3.connect('database.db')
	c =conn.cursor()
	c.execute('SELECT oid, * FROM addresses')
	records = c.fetchall()
	conn.commit()
	conn.close()

	#insert each row into tree view
	for i in records:
		tv.insert('', 'end', values=i)

	delete_btn = Button(top, text='delete a record', command=delete)
	delete_btn.grid(row=1,column=2,ipady=4, sticky=W)

	Id=Entry(top, width=10)
	Id.grid(row=1,column=1,sticky=W)
	Idl = Label(top, text='ID:')
	Idl.grid(row=1,column=0,sticky=E)


# Label arrangement
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



# Button arrangement
submit_btn = Button(root, text='Add Record to Database', command=submit)
submit_btn.grid(row=7,column=0, columnspan=2, padx=10, pady=5, ipadx=100)

show_btn = Button(root, text='Show All Record', command=show)
show_btn.grid(row=8,column=0, columnspan=2, padx=10, ipadx=124)






root.mainloop()