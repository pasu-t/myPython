from socket import *
ip = '192.168.0.101'
user = 'Public'
pswd = ''
try:
	print('establishing connection')
	connection = wmi.WMI(ip, user = user, password = pswd)
	print('connection established')
except:
	print("your username and password of " + getfqdn(ip) + " are wrong")