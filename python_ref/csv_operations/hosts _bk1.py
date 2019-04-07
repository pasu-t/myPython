import csv
#from threading import Thread
import threading
import subprocess
import os
import re
import time
path = 'C:\\Users\\Home\\Desktop\\pasi\\python_ref\\csv_operations\\hosts.csv'
with open(path) as file:
	reader = csv.reader(file)
	header = next(reader)
	data = [row for row in reader]
ip_list = []
for i in data:
	ip_list.append(i[0])
ping_status = []
def ping_ip(ip_addr):
	'''
	Functions takes ip address as a input and try to ping that ip annd gives the 
	'''
	ping = subprocess.Popen('ping '+ip_addr+' -n 10', stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
	[out, error] = ping.communicate()
	output = out.decode()
	if not error:
		ping_stats = re.search(r'.*Sent = (\d+),.*(\d+),.*(\d+)%' , output)
		c_reply = output.lower().count('ttl')
		c_timeout = output.lower().count('timed out')
		c_dest = output.lower().count('destination')
		c_loss = int(ping_stats.group(3))
		ping_status.append({ip_addr:[c_reply,c_timeout,c_dest]})
		# print(c_reply, c_timeout, c_dest)
		#print('='*40 + '\n')
	else:
		print('please check the given input')
		exit()
# for i in ip_list:
# 	ping_ip(i)
for i in ip_list:
	threading.Thread(target=ping_ip, args=(i,)).start()
for thread in threading.enumerate():
	if thread.daemon:
		continue
	try:
		thread.join()
	except RuntimeError as err:
		if 'cannot join current thread' in err.args[0]:
			continue
		else:
			raise
print(ping_status)