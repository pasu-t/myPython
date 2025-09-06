import json

with open('nobel_prize.json') as f:
	data = json.load(f)

for nobel_prize in data['prizes']:
	del nobel_prize['year']

with open('new_nobel_prize.json', 'w') as f:
	json.dump(data,f)