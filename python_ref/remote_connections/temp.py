remote_conn_status = [{'10.49.8.18': 'Success'}, {'10.49.61.127': 'Success'}, {'10.49.20.156': 'Fail'}]
ip_list = ['10.49.8.18','10.49.20.156', '10.49.61.127']
new = []
for i in ip_list:
	for j in remote_conn_status:
		try :
			new.append(j[i])
		except KeyError:
			pass
print(new)








