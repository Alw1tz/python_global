import json


# some JSON:
data = { "name":"John",
         "age":30,
         "city":"CDMX",
         "GF":"Karla" }

# parse x:
y = json.dumps(data)

# the result is a Python dictionary:
print(type(y))

x = json.loads(y)
print(x['GF'])
