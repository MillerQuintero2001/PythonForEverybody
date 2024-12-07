# Name: Miller Quintero
# Date: Dec 6, 2024
# Brief: First parsing of JSON data

import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type": "intl",
        "number" : "+1 734 303 4456"
        },
    "email" : {
            "hide" : "yes"
        }
    }'''

info = json.loads(data)
''' To can print this, is necessary understand that json.loads return data 
in a dictionary format, that could be dictionaries nested in other dictonary'''
print('Name:', info["name"])
print("Hide:", info["email"]["hide"])
print("Type:", info["phone"]["type"])
print("Number:", info["phone"]["number"])