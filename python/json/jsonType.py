import json

#list to json string
alist = [12, 57, 41, 68, 47, 62]
jsonList = json.dumps(alist)
print(jsonList)

#tuple to json string
atuple = (12, "Raghu")
jsonTuple = json.dumps(atuple)
print(jsonTuple)

#dictionary to json string
aDict = {"rollno":12, "name":"Raghu"}
jsonDict = json.dumps(aDict)
print(jsonDict)

#string to json
str = "Hello World"
jsonStr = json.dumps(str)
print(jsonStr)

#int to json
i = 25
jsonInt = json.dumps(i)
print(jsonInt)

#float to json
f = 25.256
jsonFloat = json.dumps(f)
print(jsonFloat)

#boolean to json
bool = True
jsonBool = json.dumps(bool)
print(jsonBool)

#null to json
a = None
jsonNone = json.dumps(a)
print(jsonNone)ss