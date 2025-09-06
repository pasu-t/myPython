import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages= [18, 19, 21, 25, 26, 30, 32, 38, 45, 55]
plt.hist(ages, bins=5, edgecolor='black')

# plt.legend()
plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f