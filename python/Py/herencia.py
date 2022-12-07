kitty = '''
▄   ▄
█▀█▀█
█▄█▄█
 ███  ▄▄
 ████▐█ █
 ████   █
 ▀▀▀▀▀▀▀ '''

saludo = '''
      ▄▀▄     ▄▀▄
     ▄█░░▀▀▀▀▀░░█▄
 ▄▄  █░░░░░░░░░░░█  ▄▄
█▄▄█ █░░▀░░┬░░▀░░█ █▄▄█
     M   E   O   W 
'''

babe = '''

─▄▄█────────▄▄█
─▀▀█▄▄▄▄▄▄▀─▀▀█▄▄▄▄▄▄▀
───██████─────██████
──▄█───▄█────▄█───▄█

'''

class gatitos:
	def __init__(self):
		print('# Clase Hijo ')
		self.babies = ['estrella', 'luna']
		print(f'{babe}\nMi gata tiene dos gatitos, {self.babies[0]} y {self.babies[1]}')

class gato(gatitos):

	def __init__(self):
		print('# Clase Padre ')
		# atributos de la instancia
		self.nombre = 'Kitty'
		self.tipo = 'Gatito'

	def miMascota(self):
		print(kitty)
		print(f'\nMi {self.tipo} se llama {self.nombre}')

	def saluda(self):
		print(saludo)


run = gato()
run.miMascota()
run.saluda()
r  = gatitos()

