''' 
handling

'r' > Read
'a' > Append
'w' > Write
'x' > Create

't' > 'Text'
'b' > 'Binary'
'+' > Read and write at the same time


para abrir un archivo 

file  = open('nombreDelArchivo.txt', 'rt')
# rt > read text
'''
import os 


#  crea una carpeta nueva 
# os.mkdir('py')

#  renombrar carpeta
#  nombre actual, nuevo nombre
# os.rename('py', 'python')

ruta = 'C:\\xampp\\htdocs\\files\\python\\Py\\'
fileName = 'newFile.txt'
# check if exist the file
if os.path.exists(f'{ruta+fileName}') : 
	print('File already exists')
	# write - append
	print('writting....')
	file = open(f'{ruta+fileName}', 'a')
	file.write("\nHello from the other side - Emi is Writting!! - handling.py")
	file.close()
else :
	# create a new file
	file = open(f'{ruta+fileName}', 'x')
	print('file was create!')


# read 
file = open(f'{ruta+fileName}', 'rt')
print(file.read())