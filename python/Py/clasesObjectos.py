# Clases y Objectos

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

class gato:

	def __init__(self):
		# atributos de la instancia
		self.nombre = input('Nombre > ')
		self.tipo = 'Gatito'

	def miMascota(self):
		print(kitty)
		print(f'\nMi {self.tipo} se llama {self.nombre}')

	def saluda(self):
		print(saludo)
		print(f'Meow ')

run = gato()
run.miMascota()
run.saluda()
