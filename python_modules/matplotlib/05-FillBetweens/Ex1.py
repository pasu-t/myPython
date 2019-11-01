import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

data = pd.read_csv('data.csv')
ages = data['Age']
dev_sal = data['All_Devs']
py_sal = data['Python']
js_sal = data['JavaScript']

plt.plot(ages, dev_sal, color = '#444444', linestyle='--', label='All Devs')
plt.plot(ages, py_sal, label = 'Python')

overall_median=57280
plt.fill_between(ages, py_sal, overall_median, 
	            where=(py_sal > overall_median), 
	            interpolate=True, alpha=0.25)
plt.fill_between(ages, py_sal, overall_median, 
	            where=(py_sal <= overall_median), 
	            interpolate=True,color='red', alpha=0.25)

plt.legend()
plt.title('Median Salary(USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary(USD)')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f