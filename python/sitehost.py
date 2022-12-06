
# SiteHost - Test


# for x in range(1, 101):
#     if x % 3 == 0 and x % 5 == 0 :
#             print('SiteHost')
#     elif x % 3 == 0 :
#             print('Site')
#     elif x % 5 == 0 :
#             print('Host')

#     print(x, end='\n')
        

lista = []
for x in range(1, 101):
	if x % 3 == 0 and x % 5 == 0 :
		x = 'SiteHost'
	elif x % 3 == 0 :
		x = 'Site'
	elif x % 5 == 0 :
		x = 'Host'
	lista.append(x)

print(lista)