# Python strings 

word = 'I wanna eat bananas!'

# imprime la cadena de texto
print(word)
''' muestra la posicion de una letra en especifico, 
letra e en la posicion 8 '''
print(word[8])
# imprime la palabra
for x in 'bananas':
	print(x, end='-')

# longitud de la palabra
print('\nLongitud > ',len(word))
# verifica que existe la palabra en la cadena
palabra = input('\npalabra >> ')
if palabra in word:
	print('yes, exists')
else:
	print('not here')

# Slicing string
print('show only [11:]: ', word[11:])

# upper, lower, capitalize, replace, split, count, find, index, join
p = word[12:]
print(p.upper())
print(p.lower())
print(p.capitalize())
print(p.replace('n', 't'))
print(p.split())
print('Hay ', p.count('a'), ' a en ', p)
print('\nIs wanna in Word variable? \nA parti del indice', word.find('wanna'))
print('\nIndice de eat > ', word.index("eat"))
print('--'.join(word))