
# modulos
import datetime
import calendar


'''
# %A fullname current weekDay 
# %a short version or %A
# %B fullname current Month
# %b short version or %B
# %Y fullname current year
# %y short version or %Y

# month : %m or %B >>> (%m = 06 ) and (%B = Juny)
'''

date = datetime.datetime.now()

# Dia actual 
def currentDate():
	print('\n🌼 DAMETIME 🌼\n')
	dia = date.strftime('%A')
	fecha = date.strftime('%d ・ %b ・ %y')
	print(f'::: {dia} :::\n{fecha}')

# Hora Actual 
def currentTime():
	hora = date.strftime('%H')
	minutos = date.strftime('%M')
	if int(hora) > 12 : 
		tiempo = 'PM'
		print(f'⌚ {hora} : {minutos} {tiempo}')
	else :
		tiempo = 'AM' 
		print(f'⌚ {hora} : {minutos} {tiempo}')

currentDate()
currentTime()

print('\n🌼 CALENDAR 🌼\n')
#  calendario 
if __name__ == "__main__":
    year = int(date.strftime('%Y'))
    month = int(date.strftime('%m'))
    print(calendar.month(year, month))