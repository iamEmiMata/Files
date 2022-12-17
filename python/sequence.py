
''' 
Valid Parentheses
({{}})[]()

(), [], {}

'''
# class solution:
# 	def isValid(self, sequence):
# 		while True:
# 			if '()' in sequence:
# 				sequence = sequence.replace('()', '')
# 			elif '[]' in sequence:
# 				sequence = sequence.replace('[]', '')
# 			elif '{}' in sequence:
# 				sequence = sequence.replace('{}', '')
# 			else :
# 				return not sequence

# sequence = input('>> ')
# print(f'Is {sequence} valid ? : {solution().isValid(sequence)}')


def valid(sequence):
	while True: 
		if '()' in sequence:
			sequence = sequence.replace('()', '')
		elif '[]' in sequence:
			sequence = sequence.replace('[]', '')
		elif '{}' in sequence:
			sequence = sequence.replace('{}', '')
		else:
			return not True

sequence = input('Enter sequence you want to test \n>> ')
print(f'{sequence} : {valid(sequence)}')
