import json

with open('mapped_output.json', 'r') as file:
    data = json.load(file)
    str=""
    for item in data:
        for key,values in item.items():
            str=str+key+ ':' +values +'\n'

print(data)
print(str)