import pandas as pd
from matplotlib import pyplot as plt

# print(plt.style.available)
# plt.style.use('fivethirtyeight')
plt.style.use('seaborn')
# plt.xkcd()
data = pd.read_csv('data.csv')
ages_x = data['Age']
dev_y = data['All_Devs']
py_dev_y = data['Python']
js_dev_y = data['JavaScript']

plt.plot(ages_x, py_dev_y, label='Python')

plt.plot(ages_x, js_dev_y, label='Java Script')

plt.plot(ages_x, dev_y, color = 'k', linestyle='--', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
# plt.legend(['All Devs', 'Python']) #if you don't pass label argument to plot method
plt.legend()
plt.tight_layout()
# plt.savefig('plot1.png')
plt.show()