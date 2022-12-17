
# Creating a new db with collection.

from pymongo import MongoClient

dbname = 'colores'
table = 'colorList'

# instancia
client = MongoClient('mongodb://localhost:27017/')

# nueva base de datos
db = client[dbname]

# nueva coleccion de datos
collection = db[table]
# Actualializar varios datos
collection.update_one(
	{
	"id":"2"
	},
	{
	"$set": {
		"name":"Violeta"
		}
	})

dbList = client.list_database_names()
collectionList = db.list_collection_names()
print(dbList, collectionList)
# see all
for lista in collection.find():
	print(lista.modified_count, "documents updated.")
