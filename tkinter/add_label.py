from tkinter import *

root = Tk()
# Create a label widget
mylabel1 = Label(root, text='Hello, World')
mylabel2 = Label(root, text='My name is Yipeng')
# shoving it on the screen
mylabel1.grid(row=0,column=0)
mylabel2.grid(row=1,column=0)

root.mainloop()