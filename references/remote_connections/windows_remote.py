
import subprocess
import threading
# ip = '10.49.8.46'
# username = 'admin'
# password = 'adtran1234'

ip_list = ['10.49.8.18','172.20.12.93', '10.49.8.19','10.49.8.20','172.20.12.93', '172.20.12.94', '172.20.12.95']
# username = 'ONTWIN_PC\\ONTWIN'
# password = 'adtran123'
# rdp_cmd = """If (New-Object System.Net.Sockets.TCPClient -ArgumentList '10.49.8.18',3389) { Write-Host 'RDP is open' }
# If ($? -eq $false) { Write-Host 'Something went wrong' }"""

# rdp_out = subprocess.Popen('powershell '+ rdp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# [out, error] = rdp_out.communicate()
# rdp_status = out.decode()
# print(rdp_status)
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
