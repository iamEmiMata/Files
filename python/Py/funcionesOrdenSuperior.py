
def saludar(lang):
	def saludar_es():
		print('Hola!')
	def saludar_en():
		print('Hello!')
	def saludar_fr():
		print('Salut!')

	lang_func = {
	'es': saludar_es,
	'en': saludar_en,
	'saludar_fr': saludar_fr,
	}
	return lang_func[lang]

idioma = input('Choose a lang \nes, en, fr \n> ')
saludo = saludar(idioma)
saludo()
