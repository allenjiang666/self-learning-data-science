from tkinter import *

# create a window
root = Tk()
# setup the software title
root.title('Simple caculator')


def insert_number(number):
	# don't use ~ in python as not, works in pandas
	if  not (e.get().isdigit()):
		e.delete(0,END)
	# get what is in the input box
	current_number = e.get()
	# delete what is in the input box
	e.delete(0,END)
	# insert something into the input box
	e.insert(0, str(current_number)+str(number))

def add():
	global first_num
	if e.get().isdigit():
		first_num = int(e.get())
	else:
		first_num=0
	e.delete(0,END)
	global math
	math ='add'
	e.insert(0,'+')

def sub():
	global first_num
	if e.get().isdigit():
		first_num = int(e.get())
	else:
		first_num=0
	first_num = int(e.get())
	e.delete(0,END)
	global math
	math ='sub'
	e.insert(0,'-')

def mul():
	global first_num
	if e.get().isdigit():
		first_num = int(e.get())
	else:
		first_num=0
	first_num = int(e.get())
	e.delete(0,END)
	global math
	math ='mul'
	e.insert(0,'*')

def div():
	global first_num
	if e.get().isdigit():
		first_num = int(e.get())
	else:
		first_num=0
	first_num = int(e.get())
	e.delete(0,END)
	global math
	math ='div'
	e.insert(0,'/')


def equ():
	second_num = int(e.get())
	e.delete(0,END)
	if math =='add':
		e.insert(0, first_num+second_num)
	if math =='sub':
		e.insert(0, first_num-second_num)
	if math =='mul':
		e.insert(0, first_num*second_num)
	if math =='div':
		try:
			e.insert(0, first_num/second_num)
		except ZeroDivisionError:
			e.insert(0,'Can not divide 0 !')

def cle():
	e.delete(0,END)



e = Entry(root, width=60, borderwidth=3)
e.grid(row=0,column=0, ipady= 20, columnspan=4)

button_0 = Button(root, text='0', padx=40, pady=20, command=lambda:insert_number(0))
button_1 = Button(root, text='1', padx=40, pady=20, command=lambda:insert_number(1))
button_2 = Button(root, text='2', padx=40, pady=20, command=lambda:insert_number(2))
button_3 = Button(root, text='3', padx=40, pady=20, command=lambda:insert_number(3))
button_4 = Button(root, text='4', padx=40, pady=20, command=lambda:insert_number(4))
button_5 = Button(root, text='5', padx=40, pady=20, command=lambda:insert_number(5))
button_6 = Button(root, text='6', padx=40, pady=20, command=lambda:insert_number(6))
button_7 = Button(root, text='7', padx=40, pady=20, command=lambda:insert_number(7))
button_8 = Button(root, text='8', padx=40, pady=20, command=lambda:insert_number(8))
button_9 = Button(root, text='9', padx=40, pady=20, command=lambda:insert_number(9))

button_add = Button(root, text='+', padx=39, pady=20, command=add)
button_sub = Button(root, text='-', padx=40, pady=20, command=sub)
button_mul = Button(root, text='*', padx=40, pady=20, command=mul)
button_div = Button(root, text='/', padx=41, pady=20, command=div)

button_equ = Button(root, text='=', padx=40, pady=20, command=equ)
button_cle = Button(root, text='Clear', padx=29, pady=20, command=cle)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_add.grid(row=1,column=3)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_sub.grid(row=2,column=3)

button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_mul.grid(row=3,column=3)

button_equ.grid(row=4,column=0)
button_0.grid(row=4,column=1)
button_cle.grid(row=4,column=2)
button_div.grid(row=4,column=3)





root.mainloop()