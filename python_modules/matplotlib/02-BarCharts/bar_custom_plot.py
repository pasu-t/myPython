from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')
ages_x = [25,26,27,28,29,30,31,32,33,34,35]

py_dev_y = [40496,44000,47752,51322,56200,59000,65316,68928,71371,75748,80752]
plt.plot(ages_x, py_dev_y, color='b', label='Python')

js_dev_y = [37496,42200,46722,49822,54200,55500,63316,64928,68871,70748,74752]
plt.plot(ages_x, js_dev_y, color = 'y', label='JavaScript')

dev_y = [38496,42000,46752,49322,53200,56000,62316,64928,67371,68748,73752]
plt.bar(ages_x, dev_y, color = 'k', label='All Devs')

plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')
plt.title('Median Salary (USD) by Age')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()