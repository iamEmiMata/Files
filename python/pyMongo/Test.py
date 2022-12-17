
#  Not only SQL : Mongo DB

import pymongo


dbname = 'newDb'

#  Instancia
client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client[dbname]

# Check if Db Exists
dbList = client.list_database_names()
if dbname in dbList:
	print('DB you are consulting exists!')
else :
	print(f'{dbname} not exists!')


# la base de datos no se creara si esta no tiene ademas una 
# coleccion de datos.