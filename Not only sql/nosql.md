
# SQL   ->   NoSQL
###Database -> Database
###Table, view -> Collection
###Row -> Document (Bson)
###Column -> Field
###Index -> Index
###Join -> Embedded Document
###Foreing Key -> Reference
###Partition -> Shard


## Bson Format :
- Binary-encoded serialization of Json-like documents.
- Zero or more key/value pairs are stored as a single entity
- Each entry consist of a field name, a data type and a value.
- Large elements in a Bson document are prefixed with a length field to facilitate scanning.



## Free schema :
MongoDB does not need any pre-defined data schema
 - Every document in a collection could have different data
 - Addresses NULL data fields 



## Commands :
use
db
db.collectionName.insert(doct)
db.collectionName.save(doct)
db.collectionName.update(query, update, {upsert : true})
db.collectionName.find(query, projection)
db.collectionName.findOne(query, projection)
db.collectionName.remove(query, justOne)
db.collection_name.findAndModify(query,sort,update,<new,fields,upsert)


#### Example :
> use biblioteca
'already on db biblioteca'
db.createCollection('usuarios')
{ ok: 1 }
usuarios = [{'id':'1', 'nombre':'pedro','membresia':'basica'}, {'id':'2', 'nombre':'juan','membresia':'oro'}, {'id' :'3', 'nombre' :'claudia', 'membresia' : 'plata'}]
[
  { id: '1', nombre: 'pedro', membresia: 'basica' },
  { id: '2', nombre: 'juan', membresia: 'oro' },
  { id: '3', nombre: 'claudia', membresia: 'plata' }
]
db.usuarios.insertMany(usuarios)
{ acknowledged: true,
  insertedIds: 
   { '0': ObjectId("639b640221743624583c3520"),
     '1': ObjectId("639b640221743624583c3521"),
     '2': ObjectId("639b640221743624583c3522") } }
show collections
usuarios
db.usuarios.find()
{ _id: ObjectId("639b640221743624583c3520"),
  id: '1',
  nombre: 'pedro',
  membresia: 'basica' }
{ _id: ObjectId("639b640221743624583c3521"),
  id: '2',
  nombre: 'juan',
  membresia: 'oro' }
{ _id: ObjectId("639b640221743624583c3522"),
  id: '3',
  nombre: 'claudia',
  membresia: 'plata' }
biblioteca> 
db.usuarios.insertOne({'id' : '4', 'nombre':'petra', 'membresia' : 'basica'})

db.usuarios.find()
{ _id: ObjectId("639b640221743624583c3520"),
  id: '1',
  nombre: 'pedro',
  membresia: 'basica' }
{ _id: ObjectId("639b640221743624583c3521"),
  id: '2',
  nombre: 'juan',
  membresia: 'oro' }
{ _id: ObjectId("639b640221743624583c3522"),
  id: '3',
  nombre: 'claudia',
  membresia: 'plata' }
{ _id: ObjectId("639b7f1921743624583c3523"),
  id: '4',
  nombre: 'petra',
  membresia: 'basica' }

db.usuarios.updateOne({'id':'4'},{"$set":{'nombre' : 'pillar'}})
db.usuarios.find()
{ _id: ObjectId("639b640221743624583c3520"),
  id: '1',
  nombre: 'pedro',
  membresia: 'basica' }
{ _id: ObjectId("639b640221743624583c3521"),
  id: '2',
  nombre: 'juan',
  membresia: 'oro' }
{ _id: ObjectId("639b640221743624583c3522"),
  id: '3',
  nombre: 'claudia',
  membresia: 'plata' }
{ _id: ObjectId("639b7f1921743624583c3523"),
  id: '4',
  nombre: 'pillar',
  membresia: 'basica' }

  