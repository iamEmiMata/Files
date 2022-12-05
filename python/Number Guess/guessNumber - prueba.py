# from tkinter import *
# import random

# root = Tk()
# root.geometry('300x340')
# root.resizable(0,0)
# root.configure(bg = '#63dbcd')
# root.title('Guess a number')

# # label
# Label(root,
# 	text = 'GUESS THE NUMBER',
# 	font = 'Roboto 15 bold',
# 	fg = '#000',
# 	bg = '#63dbcd').place(x = 50, y = 60)

# Label(root,
# 	text = 'Write a Number from 0 to 20',
# 	font = 'Roboto 8 ',
# 	fg = '#000',
# 	bg = '#63dbcd').place(x = 65, y = 110)

# numero = IntVar()
# # input
# number = Entry(root,
# 	width = 23,
# 	font = 'Roboto 10',
# 	textvariable = numero)
# number.insert(END, ' Enter a number')
# number.pack(padx = 40, pady = 130)

# # call function
# def choose():
# 	rango = random.randint(0, 20)
# 	oportunities = 6
# 	lessOne = 0
# 	for num in range(lessOne, oportunities):
# 		n = int(numero.get())
# 		if n == rango:
# 			Label(root, 
# 		    	text = f'Omg, You did it!\n {rango}', 
# 		    	font = 'roboto 12 bold', 
# 		    	bg = '#7332F4', 
# 		    	fg = '#FFC331').place(x= 40 , y = 250)
# 			break
# 		elif n > 20 or n < 1:
# 			oportunities = lessOne + 1
# 			Label(root, 
# 		    	text = 'Give me a number bewteen 1 to 20\nTry again!\n', 
# 		    	font = 'roboto 12 bold', 
# 		    	bg = '#7332F4', 
# 		    	fg = '#FFC331').place(x= 40 , y = 250)
# 		else:
# 			lessOne += 1
# 			Label(root, 
# 		    	text = f'No, that is not, try again...\n' + f'You lost {lessOne} oportunity\n', 
# 		    	font = 'roboto 12 bold', 
# 		    	bg = '#7332F4', 
# 		    	fg = '#FFC331').place(x= 40 , y = 250)
	
# 	if lessOne == 5:
# 		Label(root, 
# 		    	text = f'Omg, You lost!\nThe number was {rango}\n', 
# 		    	font = 'roboto 12 bold', 
# 		    	bg = '#7332F4', 
# 		    	fg = '#FFC331').place(x= 40 , y = 250)

# Button(root,
# 	width = 5,
# 	text = 'go', 
# 	font = 'roboto 11 bold', 
# 	fg = '#fff', 
# 	bg = '#260B5D', 
# 	padx = 2, command = choose).place(x=120 ,y = 170)


# root.mainloop()

from tkinter import *
import random

root = Tk()
root.geometry('300x340')
root.resizable(0, 0)
root.configure(bg='#63dbcd')
root.title('Guess a number')

# label
Label(root,
      text='GUESS THE NUMBER',
      font='Roboto 15 bold',
      fg='#000',
      bg='#63dbcd').place(x=50, y=60)

Label(root,
      text='Write a Number from 0 to 20',
      font='Roboto 8 ',
      fg='#000',
      bg='#63dbcd').place(x=65, y=110)

numero = IntVar()

# input
number = Entry(root,
               width=23,
               font='Roboto 10',
               textvariable=numero)
number.pack(padx=40, pady=130)
rango = random.randint(0, 20)
lessOne = 0
oportunities = 3

# call function
def choose(lessOne, n, rango, oportunities):
    print(lessOne, n, rango)
    if lessOne < oportunities:
        if n == rango:
            Label(root,
                  text=f'Omg, You did it!\n {rango}',
                  font='roboto 12 bold',
                  bg='#7332F4',
                  fg='#FFC331').place(x=40, y=250)
            return
        elif n > 20 or n < 1:
            Label(root,
                  text='Give me a number bewteen 1 to 20\nTry again!\n',
                  font='roboto 12 bold',
                  bg='#7332F4',
                  fg='#FFC331').place(x=40, y=250)
            globals()['lessOne'] = lessOne + 1
        else:
            Label(root,
                  text=f'No, that is not, try again...\n' + f'You lost {lessOne} oportunity\n',
                  font='roboto 12 bold',
                  bg='#7332F4',
                  fg='#FFC331').place(x=40, y=250)
            globals()['lessOne'] = lessOne + 1
    else:
        Label(root,
              text=f'Omg, You lost!\nThe number was {rango}\n',
              font='roboto 12 bold',
              bg='#7332F4',
              fg='#FFC331').place(x=40, y=250)

Button(root,
       width=5,
       text='go',
       font='roboto 11 bold',
       fg='#fff',
       bg='#260B5D',
       padx=2, command= lambda : choose(lessOne, rango, numero.get(),oportunities)).place(x=120, y=170)

root.mainloop()