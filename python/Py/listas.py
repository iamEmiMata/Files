# Listas o Vectores en  python

frutas = ["Manzana", "Bananas", "Fresas", "Mango", "Uvas", "Naranja"]

# show me
print(frutas)
# Accedo a indice : fresas
print(frutas[2])
# add me another to the array
frutas.append('Mandarinas')
# add me for index
frutas.insert(5, 'Durazno')
print(frutas)
# cambio item con el indice
frutas[0] = 'Frambuesas'
print(frutas) 
# slicing : [2] to [5]
print(frutas[2:5])
# extend list, also work with tuples
anothersFruits = ['Guayaba', 'Ciruelas']
frutas.extend(anothersFruits)
print(frutas)
# remove item from list
frutas.remove('Bananas')
print(frutas)
# iteramos segun la lista
for x in frutas:
	print(x)

print('\nlen()\n')

for x in range(len(frutas)):
	print(frutas[x])

print('\nwhile\n')
x = 0
while x < len(frutas):
	print(frutas[x])
	x += 1

print('\nlista de compresion \n')
# lista de compresion : Amo
# tambien se aplica en los set

[print(x) for x in frutas]

# agregamos a un array vacio
print('\nllenando array  \n')
array = []

#  anade solo las frutas que tengan o en la lista 
for x in frutas:
	if 'o' in x:
		array.append(x)

print(array)


print('\nlista de compresion : for + if \n')

lista = [x for x in frutas if 'u' in x]
print(lista)

print('\nlista de compresion : for + if 2 \n')

lista = [x for x in frutas if 'u' in x and x != 'Ciruelas']
print(lista)


# zip method() : Amo
print('\niterar zip : sin lista de compresion \n')
precio = [1.00, 2.00, 3.00, 4.65, 5.98, 3.02, 1.56]

for fruits, price in zip(frutas, precio):
    print(f'{fruits} > {price}')



print('\niterar zip : con lista de compresion \n')

lista = [x for x in zip(frutas, precio)]
print(lista)