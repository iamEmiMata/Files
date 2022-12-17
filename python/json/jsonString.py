import json

objeto = '[{"id":1, "color":"Azul"}, {"id":2, "color":"Verde"}]'

jsonObj = json.loads(objeto)
print(jsonObj[0])
print(jsonObj[1])