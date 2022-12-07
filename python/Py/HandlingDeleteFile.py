
import os

ruta = 'C:\\xampp\\htdocs\\files\\python\\Py\\'
fileName = 'newFile.txt'

if os.path.exists(f'{ruta+fileName}') :
  os.remove(f'{ruta+fileName}') 
  print('Archivo eliminado con exito')
else:
  print("TEl archivo que quiere eliminar no existe")