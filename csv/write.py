
# CSV Write 

import csv
ruta = 'C:\\xampp\\htdocs\\files\\python\\Py\\CSV\\'
fileName = 'newFile.csv'
with open(f'{ruta + fileName}', 'w', newline = '') as csvFile:
	write = csv.writer(csvFile)
	write.writerows('a')
	write.writerows('b')