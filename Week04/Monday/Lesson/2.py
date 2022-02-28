import json

with open('sample.json', 'r') as txt:
    data = json.loads(txt.read())

for member in data:
    if member['status'] == 'No':
        print(f"Member: {member['email']}\nVaccine: {member['typeVaccine']}")

for member in data:
    if member['status'] == 'Yes':
        print(f"{member['_id']} vaccined {member['typeVaccine']}")

for member in data:
    del member['status']
    member['name'] = 'fgaodsdifdlas'

newJson = json.dumps(data, indent=4)
print(type(newJson))