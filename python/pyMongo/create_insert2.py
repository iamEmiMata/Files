
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

# inserta datos en la collecion
# Insertar varios al mismo tiempo
data = [
{
"id" : "1",
"name" : "Blanco"
},
{
"id" : "2",
"name" : "Rojo"
},
{
"id" : "3",
"name" : "Negro"
},
{
"id" : "4",
"name" : "Azul"
}]

# checa si existe o no
collection.insert_many(data) # add many obj
dbList = client.list_database_names()
collectionList = db.list_collection_names()

# collection.find_one() : see only one
print(dbList, collectionList)
# see all
for lista in collection.find():
 print(lista)