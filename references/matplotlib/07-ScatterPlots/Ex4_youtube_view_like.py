import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('seaborn')
data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes,
	edgecolor = 'black', linewidth = 1, alpha=0.75)

plt.xscale('log')
plt.yscale('log')

plt.title('Trending youtube videos')
plt.xlabel('View Count')
plt.ylabel('Total likes')
plt.tight_layout()
plt.show()