from tkinter import *
import string
import random
import time

root = Tk()
root.geometry('400x300')
root.resizable(0,0)
root.configure(bg='#5E17EB')
root.title('Password Generator')


Label(root,
	text = '*******',
	font = 'Roboto 25 bold',
	fg = '#fff',
	bg = '#5E17EB').place(x = 160, y = 20)

Label(root,
	text = 'Password Generator',
	font = 'Roboto 20 bold',
	fg = '#fff',
	bg = '#5E17EB').place(x = 70, y = 60)

longt = IntVar()

#input
length = Entry(root,
	width = 23,
	font = 'Roboto 11',
	textvariable = longt)
length.insert(END, ' Enter a length')
length.pack(padx = 40, pady = 130)

# Function
def generator(longitud):
	simbolos= '$@#^%&*!~?/+'
	simb = random.choice(simbolos)
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	digit = string.digits

	characters = lower + upper + digit + simb
	passw = ''.join(random.sample(characters, longitud))
	Label(root, 
    	text = ' ' + passw + ' ', 
    	font = 'roboto 12 bold', 
    	bg = '#7332F4', 
    	fg = '#FFC331').place(x= 110 , y = 250)

def password():
	longitud = int(longt.get())
	if longitud is str(longitud).isnumeric():
		Label(root, 
    	text = 'Please give me just integers numbers', 
    	font = 'roboto 12', 
    	bg = '#7332F4', 
    	fg = '#fff').place(x= 70 , y = 250)
	else:
		generator(longitud) # Call function generator

# call function password
Button(root,
	width = 10,
	text = 'CREATE', 
	font = 'roboto 11 bold', 
	fg = '#fff', 
	bg = '#260B5D', 
	padx = 2, command = password).place(x=145 ,y = 180)

root.mainloop()