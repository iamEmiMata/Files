
# Creating a new db with collection.

from pymongo import MongoClient

dbname = 'books'
table = 'bookList'

# instancia
client = MongoClient('mongodb://localhost:27017/')

# nueva base de datos
db = client[dbname]

# nueva coleccion de datos
collection = db[table]

# inserta datos en la collecion

# Insertar solo 1
data = { 
"id" : "1",
"name" : "Viaje al fin de la noche", 
"author" : "Louis-Ferdinand Céline",
"year" : "1932"
}


# Insertar varios al mismo tiempo
data1 = [
{
"id" : "2",
"name" : "Orgullo y prejuicio",
"author" : "Jane Austen",
"year" : "1813" 
},
{
"id" : "3",
"name" : "El extranjero",
"author" : "Albert Camus",
"year" : "1942"
},
{
"id" : "4",
"name" : "La magia del silencio",
"author" : "Kankyo Tanner",
"year" : "2017"
}]

# checa si existe o no
collection.insert_one(data) # add 1 obj
collection.insert_many(data1) # add many obj
dbList = client.list_database_names()
collectionList = db.list_collection_names()

# collection.find_one() : see only one
print(dbList, collectionList)
# see all
for lista in collection.find():
 print(lista)