# objects in python or dictionaries


library = [ 
{
	'name' : 'Viaje al fin de la noche',
	'author' : 'Louis-Ferdinand Céline',
	'year' : 1932
}, 
{
	'name' : 'Orgullo y prejuicio',
	'author' : 'Jane Austen',
	'year' : 1813
},
{
	'name' : 'El extranjero',
	'author' : 'Albert Camus',
	'year' : 1942
},
{
	'name' : 'Nostromo',
	'author' : 'Joseph Conrad',
	'year' : 1904
},

]

# acceder a el primer objeto de la lista
print(library[1])

# acceder al primer item del primer objeto
print(library[1]['name'])

# otra manera de llamar un item dentro del objeto.
print(library[0].get('name'))

# acceder a keys and items 
print('\n Keys')
print(library[0].keys())
print('\n Items')
print(library[0].items())


# cambiar un valor
print('\n Change value')
print(library[3])
library[3]['year'] = 2022
print(library[3])

# eliminar un valor
print('\n Remove a value')
print(library[0])
del library[0]['year']
print(library[0])

# check if exist a value
print('\n Check if exists')
if 'author' in library[2]:
	print('yes', library[2]['author'])
else:
	print('not exists')


# add an item
print('\n Add a value')
print(library[0])
library[0]['color'] = 'Verde'
print(library[0])

# nested 

i1 =	{
		'color' : 'while',
		'code' : '#fff'
}
i2 = {
		'color' : 'black',
		'code' : '#000'
}
i3 =	{
		'color' : 'red',
		'code' : '#ff0000'
}
i4 =	{
		'color' : 'gray',
		'code' : '#ddd'
}


new = {
	item1 : i1,
	item2 : i2,
	item3 : i3,
	item4 : i4
}

print(new[1]['item1'])