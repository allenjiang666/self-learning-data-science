from tkinter import *
from PIL import ImageTk, Image
import os


imgs=[]
size=(600,600)
img_num = 0
rotation=0
# '.' means the current directory
for i,f in enumerate(os.listdir('pics/')):
	# f is a str which represent file name
	if f.endswith('.jpeg'):
		# relative to the .py file
		img_i = Image.open("pics/"+f)
		img_i.thumbnail(size)
		imgs.append(img_i)



root = Tk()
root.title('Simple Image viewer')

# Convert to tk formatted before using the list in a function


def show_image():
	global my_label
	global status_bar
	# Have to make this variable global, otherwise it won't show
	global img
	# somehow .rotate can't not be used outside of the prenticis
	img = ImageTk.PhotoImage(imgs[img_num].rotate(rotation))
	my_label = Label(image=img)
	my_label.grid(row=0, column=0, columnspan=4)

	# add status bar. bd means border, relief means the lable is sunken, anchor means where you want to put the text
	status_bar = Label(root, text= f'Image {str(img_num)} of {str(len(imgs))}', bd=1, relief=SUNKEN, anchor=E)
	status_bar.grid(row=2, column=0, pady=10, columnspan=4, sticky=E+W)
	# when reach first image, can't go further back
	if img_num==0:
		button_back['state']=DISABLED
	else:
		button_back['state']=NORMAL

	# when reach last image, can't go further more.
	if img_num==len(imgs)-1:
		button_forw['state']=DISABLED
	else:
		button_forw['state']=NORMAL

	

def forward():
	#  use the global keyword ifchange a global variable inside a function.
	global img_num
	global my_label
	img_num += 1
	my_label.grid_forget()
	show_image()




def backward():
	# use the global keyword if change a global variable inside a function.
	global img_num
	global my_label
	img_num -= 1
	my_label.grid_forget()
	show_image()

def turn_left():
	global rotation
	global my_label
	# change rotation +90 degrees
	rotation +=90
	my_label.grid_forget()
	show_image()

def turn_right():
	global rotation
	global my_label
	# change rotation -90 degrees
	rotation -= 90
	my_label.grid_forget()
	show_image()

	


button_forw = Button(root, padx=30, pady =5, text='>>',command=forward)
button_back = Button(root, padx=30, pady =5, text='<<',command=backward)

button_left = Button(root, padx=15, pady =5, text='rotate left',command=turn_left)
button_right = Button(root, padx=15, pady =5, text='rotate right',command=turn_right)


button_forw.grid(row=1, column=3, pady=10)
button_back.grid(row=1, column=0, pady=10)
button_left.grid(row=1, column=1, pady=10)
button_right.grid(row=1, column=2, pady=10)


show_image()

root.mainloop()