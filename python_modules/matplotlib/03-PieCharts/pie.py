from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [120, 80, 30, 40]
labels = ['sixty', 'forty', 'ex1', 'ex2']
# colors = ['blue', 'red', 'yellow', 'green']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']
plt.pie(slices, labels=labels, colors=colors, autopct = '%1.1f%%', wedgeprops = {'edgecolor' : 'black'})
# plt.pie(slices, labels=labels, wedgeprops = {'edgecolor' : 'black'})
plt.title('Most Popular Languages')
plt.tight_layout()
plt.savefig('pie.png')
plt.show()

# Colors:
# Blue = #008fd5
# Red = #fc4f30
# Yellow = #e5ae37
# Green = #6d904f
