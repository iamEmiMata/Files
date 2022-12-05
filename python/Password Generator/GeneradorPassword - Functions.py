import random
import time
import string


def intro():
	msg = '''
	++++++++++++++++++++++++

		PASSWORD GENERATOR

	
	# To create a safe password 
	# please write a length.

	++++++++++++++++++++++++

	'''

	print(msg)
	time.sleep(1)

def generator(longitud):
	simbolos= ['$', '#', '*', '@', '?', '!', '&', '%']
	simb = random.choice(simbolos)
	lower = string.ascii_lowercase
	upper = string.ascii_uppercase
	digit = string.digits

	characters = lower + upper + digit + simb
	passw = ''.join(random.sample(characters, longitud))
	print(f'We have generated this password {passw}')


def password():
	longitud = int(input('Enter a length for your password\n>	'))
	if longitud is str(longitud).isnumeric():
		print('Please give me just integers numbers')
	else:
		print('We are working in create your password')
		time.sleep(2)
		print('We are almost ready!')
		time.sleep(1)
		generator(longitud)

intro()
password()