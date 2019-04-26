import csv
import threading
import paramiko
import warnings
ip_list = []
hosts_name = []
ping_status = []
ping_health = []
ip_list_windows = []
ip_list_linux = []
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
def ssh_connect(ssh_conn_list):
	'''
	ssh_conn_list is the list object contains ip,user,password elements [ipaddresss, user, password]
	Tries ssh remote connection and appends the status to linux_remote_check list variable
	'''
	try:
	    ssh = paramiko.SSHClient()
	    warnings.filterwarnings(action='ignore',module='.*paramiko.*') # To eliminate display of warning statements w.r.t cryptography version used by paramiko module
	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    ssh.connect(ssh_conn_list[0],username=ssh_conn_list[1],password=ssh_conn_list[2])
	    print("Connected to", host)
	    remote_conn_status.append({ssh_conn_list[0] : 'Success'})
	except paramiko.AuthenticationException:
	    print("Failed to connect to" , host , "due to wrong username/password")
	    remote_conn_status.append({ssh_conn_list[0] : 'Fail'})
	    #exit(1)
	except Exception as e:
	    print(e)
	    remote_conn_status.append({ssh_conn_list[0] : 'Fail'}) 

def start_linux_remote_check():
	'''
	function starts the simultaneous ping to the ip address in the list by creating thread objects.
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
start_linux_remote_check()
print(remote_conn_status)