#сериализация и десериализация на json
import json

data = {
    'a' : [3, 4],
    'b' : [6, 8]
}

with open('data.json', 'w') as dj:
    json.dump(data, dj)

with open('data.json', 'r') as dj:
    loaded = json.load(dj)  
    print(loaded)