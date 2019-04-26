import csv
import threading
import subprocess
import paramiko
import warnings
import logging

ip_list = []
ip_list_windows = []
ip_list_linux = []
hosts_name = []
ping_health = []
remote_conn_status = []
with open('hosts.csv', 'r') as hosts_file:
	hosts_reader = csv.DictReader(hosts_file)
	for line in hosts_reader:
		ip_list.append(line['ip_address'])
		hosts_name.append(line['host_name'])
		if line['os'] == 'windows':
			ip_list_windows.append(line['ip_address'])
		else:
			ip_list_linux.append([line['ip_address'],line['user'],line['password']])
	ping_health = [' ' for _ in range(len(ip_list))]

def windows_remote_check(ip_addr):
	'''
	this function verifies whether remote connection is enabled for the given ip address of windows machine
	'''
	rdp_cmd = """If (New-Object System.Net.Sockets.TCPClient -ArgumentList """ + ip_addr + """,3389) { Write-Host 'RDP is open' }
	If ($? -eq $false) { Write-Host 'Something went wrong' }"""
	rdp_out = subprocess.Popen('powershell '+ rdp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	[out, error] = rdp_out.communicate()
	rdp_status = out.decode()
	if 'RDP is open' in rdp_status:
		remote_conn_status.append({ip_addr : 'Success'})
		#print(rdp_status)
	else:
		print('A remote connection attempt failed to ',ip_addr)
		#print(error.decode())
		remote_conn_status.append({ip_addr :'Fail'})
# for each in ip_list:
# 	windows_remote_check(each)

def start_windows_remote_check():
	'''
	function starts the simultaneous rdp check to the ip address in the list by creating thread objects.
	Then it wait till all the threads to complete their tasks.
	It will igonre the dummy threads which may exists.
	'''
	for i in ip_list_windows:
		threading.Thread(target=windows_remote_check, args=(i,)).start()
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

def ssh_connect(ssh_conn_list):
	'''
	ssh_conn_list is the list object contains ip,user,password elements [ipaddresss, user, password]
	Tries ssh remote connection and appends the status to linux_remote_check list variable
	'''
	try:
	    ssh = paramiko.SSHClient()
	    warnings.filterwarnings(action='ignore',module='.*paramiko.*') # To eliminate display of warning statements w.r.t cryptography version used by paramiko module
	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    paramiko.util.log_to_file("Exception.log")
	    ssh.connect(ssh_conn_list[0],username=ssh_conn_list[1],password=ssh_conn_list[2])
	    print("Connected to", ssh_conn_list[0])
	    remote_conn_status.append({ssh_conn_list[0] : 'Success'})
	except paramiko.AuthenticationException:
	    print("Failed to connect to" , ssh_conn_list[0] , "due to wrong username/password")
	    remote_conn_status.append({ssh_conn_list[0] : 'Fail'})
	except Exception as e:
	    #print(e)
	    remote_conn_status.append({ssh_conn_list[0] : 'Fail'}) 
	finally:
		if ssh: 
			ssh.close()

def start_linux_remote_check():
	'''
	function starts the simultaneous ssh to the ip address in the list by creating thread objects.
	Then it wait till all the threads to complete their tasks.
	It will igonre the dummy threads which may exists.
	'''
	for i in ip_list_linux:
		threading.Thread(target=ssh_connect, args=(i,)).start()
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

# def create_csv():
# 	'''
# 	this function creates a csv file with ip_list, hostname , ping health and remote connectivity when called
# 	'''
# 	print('started creating csv file for host status !!!')
# 	with open('hosts_status.csv', 'w') as new_file:
# 		fieldnames = ['ip_address', 'host_name', 'ping_health', 'remote_conn_check']
# 		output_lines = tuple(map(lambda a,b,c,d: [a,b,c,d],ip_list, hosts_name, ping_health, remote_conn_status))
# 		csv_writer = csv.writer(new_file)
# 		csv_writer.writerow(fieldnames)
# 		for line in output_lines:
# 			csv_writer.writerow(line)

start_windows_remote_check()
start_linux_remote_check()
print(remote_conn_status)
print(ip_list)
#create_csv()