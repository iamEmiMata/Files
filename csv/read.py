
#  CSV Read 

import csv 
ruta = 'C:\\xampp\\htdocs\\files\\python\\Py\\CSV\\'
fileName = 'newFile.csv'
with open(f'{ruta + fileName}', newline = '') as csvFile:
	spamReader = csv.reader(csvFile, delimiter = ' ', quotechar = '|')
	for row in spamReader:
		print(', '.join(row))