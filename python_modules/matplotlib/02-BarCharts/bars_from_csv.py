import csv
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

with open('data.csv') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	languages_counter = Counter()
	for row in csv_reader:
		languages_counter.update(row['LanguagesWorkedWith'].split(';'))
		# print(row['LanguagesWorkedWith'].split(';'))

# print(languages_counter)
# print(languages_counter.most_common(15))
languages = []
popularity = []
for item in languages_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

languages.reverse()
popularity.reverse()
plt.barh(languages,popularity)

plt.xlabel('Number of people who use')
# plt.ylabel('Programming languages')
plt.title('Most Popular Languages')
plt.tight_layout()
plt.savefig('multibar.png')
plt.show()
