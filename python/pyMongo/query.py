
from pymongo import MongoClient

dbname = 'books'
objectColl = 'bookList'

client = MongoClient('mongodb://localhost:27017')
db = client[dbname]
collection = db[objectColl]

query = {
	"name" : "El extranjero" 
}

data = collection.find(query)
for d in data:
	print(d)