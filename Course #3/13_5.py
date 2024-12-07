# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: Parsing JSON data with lists and dictonaries

import json

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
# We got a list of dictionaries, that was indicated by '[]' in the JSON data
print('User count:', len(info))

for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute:', item['x'])