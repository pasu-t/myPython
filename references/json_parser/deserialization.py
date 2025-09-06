import json

with open('nobel_prize.json') as f:
	data = json.load(f)

for nobel_prize in data['prizes']:
	print(nobel_prize['year'], nobel_prize['category'])