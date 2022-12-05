# Ejemplo #3
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
# 53, 59, 61, 67, 71, 73, 79, 83, 89 y 97.

def primeFinder():
	msg = ''' 
	| PRIME FINDER |
	'''
	n = int(input(f'{msg}\nIs it a number Prime? >  '))
	if n %2 != 0:  
		print(True)
	else:
		print(False)
primeFinder()