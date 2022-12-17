
# find() in Not only SQL

from pymongo import MongoClient

dbname = 'books'
objectColl = 'bookList'

client = MongoClient('mongodb://localhost:27017')
db = client[dbname]
collection = db[objectColl]


for item in collection.find({'id' : '1'}):
	print(item)