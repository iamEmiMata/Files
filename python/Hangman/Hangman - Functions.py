# EL AHORCADO
import random
import time

listaPalabras = [  'serendipia', 'inefable', 'efimero', 
'inconmensurable', 'resiliencia', 'reciprocidad', 'petricor', 
'epifania', 'imprescindible', 'iridiscencia' ]

def intro():
	msg = ''' 

   		 E L   A H O R C A D O 

	Tienes 5 oportunidades para adivinar la palabra secreta, 
	de lo contrario perderas.

	'''
	print(msg)
	time.sleep(1)

def mostrarMenu(categoria):
	for clave in sorted(categoria):
		print(f'{clave} -> {categoria[clave][0]}')

def leerCategoria(categoria):
	# Walrus ->  :=
	while (a := input('>	')) not in categoria:
		print('Ingresaste una opcion no valida, intenta otra vez.')
	return a

def categoriaSel(op, categoria):
	categoria[op][1]()

def runMenu(categoria, salida):
	op = None
	while op != salida:
		mostrarMenu(categoria)
		op = leerCategoria(categoria)
		categoriaSel(op, categoria)
		print()

def switch():
	categoria = {
		'1' : ('Comenzar a jugar', start),
		'2' : ('Salir', salir)
	}

	runMenu(categoria, '2')

def salir():
	time.sleep(0.5)
	print('Gracias por jugar El Ahorcado!')

def start():
	print('Buena eleccion, Vamos a jugar!')
	palabraSecreta = random.choice(listaPalabras)

	vida = 5
	letrasCorrectas = [' ', ',','.']
	print(' ' + '_ ' * len(palabraSecreta) + ' ')

	while True:
		while True:
			letra = input('\nAñade una letra >   ').lower()
			if (len(letra) > 0 and letra.isnumeric()):
				print('Dame una letra real, esto no es una letra!')
			else:
				if letra.lower() in letrasCorrectas:
					print('Estas repitiendo letras??\n')
					time.sleep(0.5)
					print('Intenta de nuevo... ')
					time.sleep(0.5)

				else:
					letrasCorrectas.append(letra)
					if letra.lower() in palabraSecreta:
						print('\n')
						break
					else:
						vida -= 1
						print('\nAcabas de perder una vida, Letra equivocada')
						print(f'Te quedan {vida} vidas\n')
						break

		if vida == 0:
			time.sleep(0.5)
			print(f'Haz perdido!\nPalabra secreta : {palabraSecreta}')
			break

		actual = ''
		faltaLetra = 0
		for letras in palabraSecreta:
			if letras in letrasCorrectas:
				actual += letras 
			else:
				actual += '_' 
				faltaLetra += 1

		print(actual)
		if faltaLetra == 0: 
			time.sleep(1)
			print(f'Excelente.\tHaz adivinado!')
			break


intro()
if __name__ == '__main__':
    switch()