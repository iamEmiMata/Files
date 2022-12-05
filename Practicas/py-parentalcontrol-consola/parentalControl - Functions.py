movie = {
	'Name' : 'The Gray Man',
	'Duration' : '2h 2m',
	'Year' : '2022',
	'Gender' : 'Action/Suspense',
	'Control' :'PG-13',
	'Direction' : ['Anthony Russo', 'Joe Russo'],
	'Description' : "Six, a highly-skilled assassin in the deep-cover Sierra program of the... Read More",
	'Rating' : '6,5/10',
	'Comment' : '89% liked this movie'
}

def info():
	print(':: M O V I E :: \n')
	for key, value in movie.items():
		print(f':: {key} : {value}')

def checkAge():
	print('Your parental control allow this content.\n')
	age = int(input('Enter your age\n>	'))
	if age > 17 or age == 18:
		print('Movie is chargin... ')
	elif  age < 17 and age > 13 : 
		print('This movie contains explicit scenes.\nRemember to be accompanied by an adult.') 
		print('Movie is chargin... ')
	else:
		print('These types of content are not allowed for children under 13 years of age')


def paremsAllow():
	if movie['Control'] == 'PG-13':
		Allowed = input('\n\n:: CONTROL PARENTAL ::\nDo you want to allow this content ( Y / N ) \n >  ')
		if Allowed == 'Y' or Allowed == 'y':
			Allowed = True
			checkAge()
		else :
			print('\nParental control is blocking the content.\nTo view this content requires changes to your settings')
	else:
		print('\nThis movie does not require parental control')

info()
paremsAllow()
