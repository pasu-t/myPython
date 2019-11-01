import random
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')

def animate(i):
	data = pd.read_csv('data.csv')
	x  = data['x_value']
	y1 = data['total_1']
	y2 = data['total_2']
	plt.cla() #helps not to change the color for every plot
	plt.plot(x, y1, label = 'channel 1')
	plt.plot(x, y2, label = 'channel 2')
	plt.legend(loc = 'upper left')
	plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval = 1000)

# plt.tight_layout()
plt.show()
