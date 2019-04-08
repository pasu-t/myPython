ip = '172.20.12.151'
user = ''
pswd = ''
from socket import *
try:
	print('establishing connection')
	connection = wmi.WMI(ip, user = user, password = pswd)
	print('connection established')
except:
	print("your username and password of " + getfqdn(ip) + " are wrong")