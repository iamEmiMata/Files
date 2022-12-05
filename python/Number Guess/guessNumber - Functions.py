# Adivina el numero
import random
import time

def intro():
	msg = ''' 
	++++++++++++++++++++++++++++++++++++

	G U E S S     T H E      N U M B E R

	You only have 5 oportunities 
	to guess the number from 1 to 20.
	
	# Let's to Play!

	++++++++++++++++++++++++++++++++++++
	'''
	print(msg)
	time.sleep(1)

def choose():
	rango = random.randint(0, 20)
	oportunities = 6
	lessOne = 0
	for num in range(lessOne, oportunities):
		n = int(input('Enter a number >	 '))
		if n == rango:
			time.sleep(1)
			print('\nOmg, You did it!')
			print(f'The number was {rango} \nFollow me in insta -> @_emimata')
			break
		elif n > 20 or n < 1:
			oportunities = lessOne + 1
			print('Give me a number bewteen 1 to 20\nTry again!\n')
		else:
			lessOne += 1
			print('No, that is not, try again...')
			print(f'You lost {lessOne} oportunity\n')
			time.sleep(0.2)
	
	if lessOne == 5:
		print(f'Omg, You lost!\nThe number was {rango}\n\nFollow me in insta -> @_emimata')

intro()
choose()


