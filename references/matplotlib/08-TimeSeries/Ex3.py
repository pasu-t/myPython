import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

data = pd.read_csv('data.csv')
#below two lines will add some robustness interms of sorting
data['Date'] = pd.to_datetime(data['Date']) #convert date column values from string format to datetime format 
data.sort_values('Date', inplace=True) #this will sort the dates in order if they are not in orderly fashion

price_date = data['Date']
price_close = data['Close']

plt.plot_date(price_date, price_close, linestyle = 'solid')
plt.gcf().autofmt_xdate()
# date_format = mpl_dates.DateFormatter('%b %d %Y')
# plt.gca().xaxis.set_major_formatter(date_format)

plt.title('Bitcoin Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.tight_layout()
plt.show()