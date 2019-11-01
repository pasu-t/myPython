import pandas as pd
from matplotlib import pyplot as plt

# print(plt.style.available)
plt.style.use('seaborn')

fig, ax = plt.subplots()

data = pd.read_csv('data.csv')
ages_x = data['Age']
dev_y = data['All_Devs']
py_dev_y = data['Python']
js_dev_y = data['JavaScript']

ax.plot(ages_x, py_dev_y, label='Python')

ax.plot(ages_x, js_dev_y, label='Java Script')

ax.plot(ages_x, dev_y, color = 'k', linestyle='--', label='All Devs')

ax.set_xlabel('Ages')
ax.set_ylabel('Median Salary (USD)')
ax.set_title('Median Salary (USD) by Age')
ax.legend()
plt.tight_layout()
# plt.savefig('plot1.png')
plt.show()