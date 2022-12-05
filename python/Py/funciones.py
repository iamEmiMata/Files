# Functions

# basic
def hello():
	nombre = input('Tu nombre >> ')
	print('Hi,', nombre)


# hello()

# con parametros 
def hello(name):
	print(f'Hola {name}')


# name = input('Tu nombre >>>  ')
# hello(name)


def suma(*num):
    print(sum(num))

# suma(1,2,3,4)


def nombres(**names):
	for key, value in names.items():
		x = input('>> ')
		if x in names:
			print(key, "=", value)
		else:
			print(False)

names = {"Luis":'20', "Pedro" : '21', "Ramon" : '22'}
# nombres(**names)


# Function Annotations

def filtrar_pares(salida: 'list' = []) -> 'list':
    return [i for i in salida if i%2 == 0]

# print(filtrar_pares([1, 2, 3, 4, 5, 6]))

def filtrar_nombres(salida: 'list' = []) -> 'list':
	return [i for i in salida if 'e' in i]

# print(filtrar_nombres(['erika', 'maria', 'luisa', 'petra', 'sofia']))


def colors(salida: 'lista' = []) -> 'lista':
	return [print(x) for x in salida if 'u' in x]

colors(['verde', 'morado', 'azul', 'blanco'])

