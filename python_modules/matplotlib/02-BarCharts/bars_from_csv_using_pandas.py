# import csv
import pandas as pd
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

languages_counter = Counter()
for response in lang_responses:
	languages_counter.update(response.split(';'))
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
