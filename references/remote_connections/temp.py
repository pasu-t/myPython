# remote_conn_status = [{'10.49.8.18': 'Success'}, {'10.49.61.127': 'Success'}, {'10.49.20.156': 'Fail'}]
# ip_list = ['10.49.8.18','10.49.20.156', '10.49.61.127']
# new = []
# for i in ip_list:
# 	for j in remote_conn_status:
# 		try :
# 			new.append(j[i])
# 		except KeyError:
# 			pass
# print(new)
# [{'172.20.12.92': 'Fail'}, {'10.49.8.18': 'Fail'}, {'10.49.61.125': 'Fail'}, {'10.49.20.156': 'Fail'}, {'10.49.20.152': 'Fail'}, {'10.49.61.126': 'Fail'}, {'10.49.61.128': 'Fail'}, {'10.49.61.127': 'Fail'}, {'10.49.61.139': 'Fail'}]
# ['10.49.20.156', '10.49.20.152', '10.49.61.125', '10.49.61.126', '10.49.61.127', '10.49.61.128', '10.49.61.139', '10.49.8.18', '172.20.12.92']
import subprocess
import re
def ping_ip(ip_addr):
	'''
	Functions takes ip address as a input and try to ping that ip annd appends the results to ping_status
	'''
	ping = subprocess.Popen('ping '+ip_addr+' -n 4', stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
	[out, error] = ping.communicate()
	output = out.decode()
	if not error:
		ping_stats = re.search(r'.*Sent = (\d+),.*(\d+),.*(\d+)%' , output)
		c_reply = output.lower().count('ttl')
		c_timeout = output.lower().count('timed out')
		c_dest = output.lower().count('destination')
		c_loss = int(ping_stats.group(3))
		#ping_status.append({ip_addr:[c_reply,c_timeout,c_dest]})
		print(c_reply, c_timeout, c_dest)
	else:
		print('please check the given input')
		exit()
ping_ip('172.20.13.12')





