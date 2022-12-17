# ctrl + alt + B // consola repl

# Permutations ABC

#  Version 2
def permutaciones(letras):
	if len(letras) == 0:
		return []
	elif len(letras) == 1:
		return [letras]

	arr = []
	for index in range(len(letras)):
		nuevoIndice = letras[index] # completa el indice contando de 1 en 1
		# indice = letras[index] + letras[:index] + letras[index+1:] # completa pero repitiendo letras
		indice = letras[:index] + letras[index+1:]
		for i in permutaciones(indice):
			# arr.append(list(nuevoIndice)+i)
			arr.append([nuevoIndice] + i)
		# print(indice)
	return arr

lista = ['A', 'B', 'C']
for letra in permutaciones(lista):
	print(letra)


print('\n')

# Version 1
def permutations():
	lettersList = 'ABC'
	for letter in range(len(lettersList)):
		letterIndex = lettersList[letter] + lettersList[:letter] + lettersList[letter+1:] 
		print(letterIndex.split())
permutations()
