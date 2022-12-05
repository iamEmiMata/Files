import random

class adivinaNum():
	def __init__(self):
	    self.intentos = 1
	    self.vida = 4
	    self.numRandom = random.randint(0, 10)

	def juego(self):
		for n in range(self.intentos, self.vida):
			self.numero = int(input('> '))
			if self.numero == self.numRandom:
				print(f'Ganaste! El numero era {self.numRandom}')
				break
			elif self.numero > 10 or self.numero < 1:
				print('Ingresa un numero entre 1 y 10')
			elif self.numero == str(self.numero):
				self.intentos = self.intentos + 1
				print('Esto no es un numero')
			else:
				print(f'\nAcabas de perder {self.intentos} intento')
				self.intentos = self.intentos + 1
				print('Agrega un numero nuevo\n')
			print(self.numRandom, self.numero, self.intentos)
			if self.intentos == self.vida:
				print(f'Perdiste! El numero era {self.numRandom}')
p = adivinaNum()
p.juego()