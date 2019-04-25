import csv
import threading
import subprocess

with open('hosts.csv', 'r') as hosts_file:
	hosts_reader = csv.DictReader(hosts_file)
	for line in hosts_reader:
		ip_list.append(line['ip_address'])
		hosts_name.append(line['host_name'])
	remote_conn_check = [' ' for _ in range(len(ip_list))]
	
windows_remote_status = []
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
		windows_remote_status.append({ip_addr : 'Success'})
		#print(rdp_status)
	else:
		print('A remote connection attempt failed to ',ip_addr)
		#print(error.decode())
		windows_remote_status.append({ip_addr :'Fail'})
# for each in ip_list:
# 	windows_remote_check(each)

def start_remote_check():
	'''
	function starts the simultaneous ping to the ip address in the list by creating thread objects.
	Then it wait till all the threads to complete their tasks.
	It will igonre the dummy threads which may exists.
	'''
	for i in ip_list:
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
start_remote_check()
print(windows_remote_status)