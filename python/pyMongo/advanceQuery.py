from pymongo import MongoClient

dbname = 'books'
objectColl = 'bookList'

client = MongoClient('mongodb://localhost:27017')
db = client[dbname]
collection = db[objectColl]

# mayor que
query1 = { 
	"year": { "$gt": "1942" } 
} 

# para ver todos los que contengan la palabra clave
query2 = {
	"year": { "$regex": "^1" }
}

data = collection.find(query2)
for d in data:
	print(d)