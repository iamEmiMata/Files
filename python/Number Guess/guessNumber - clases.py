
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

number = IntVar()

# input
inputNum = Entry(root,
               width=23,
               font='Roboto 10',
               textvariable=number)
inputNum.pack(padx=40, pady=130)
numRandom = random.randint(0, 20)
intentos = 1
vida = 4

# call function
def choose(intentos, xNum, numRandom, vida):
    print(intentos, xNum, numRandom)
    if intentos < vida:
        if xNum == numRandom:
            Label(root,
                  text=f'Omg, You did it! The number was {numRandom}',
                  fg='#000').place(x=40, y=250)
            return
        elif xNum > 20 or xNum <= 1:
            Label(root,
                  text='Give me a number bewteen 1 to 20, Try again!',
                  fg='#000').place(x=40, y=250)
            globals()['intentos'] = intentos + 1
        else:
            Label(root,
                  text=f'No, try again.' + f'You lost {intentos} oportunity',
                  fg='#000').place(x=40, y=250)
            globals()['intentos'] = intentos + 1
    else:
        Label(root,
              text=f'Omg, You lost! The number was {xNum}',
              fg='#000').place(x=40, y=250)

Button(root,
       width=5,
       text='Entry',
       font='roboto 11 bold',
       fg='#000',
       padx=2, command= lambda : choose(intentos, numRandom, number.get(),vida)).place(x=120, y=170)

root.mainloop()