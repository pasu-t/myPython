import csv
import threading
import subprocess
import os
import re
import time
import paramiko
import warnings
import smtplib
from email.message import EmailMessage

class Host_status():
	
	def __init__(self):
		self.list_contacts = ['pasupathi.thumburu@gmail.com', 'pasupathi.thumbur@adtran.com']
		self.list_files = ['hosts_status.csv']
		self.ip_list = []
		self.hosts_name = []
		self.ping_status = []
		self.ping_health = []
		self.ip_list_windows = []
		self.ip_list_linux = []
		self.remote_conn_status = []
		self.final_remote_conn_status = []

		try:
			with open('hosts.csv', 'r') as hosts_file:
				hosts_reader = csv.DictReader(hosts_file)
				for line in hosts_reader:
					self.ip_list.append(line['ip_address'])
					self.hosts_name.append(line['host_name'])
					if line['os'] == 'windows':
						self.ip_list_windows.append(line['ip_address'])
					else:
						self.ip_list_linux.append([line['ip_address'],line['user'],line['password']])
		except FileNotFoundError:
			print('Input hosts.csv file is not found.Please check.')
			exit()

		self.start_ping()
		self.check_ping_health()
		self.start_windows_remote_check()
		self.start_linux_remote_check()
		self.get_remote_conn_status()
		self.create_csv()
		self.send_email(self.list_files,self.list_contacts)
		
	def ping_ip(self,ip_addr):
		'''
		Functions takes ip address as a input and try to ping that ip annd appends the results to ping_status
		'''
		ping = subprocess.Popen('ping '+ip_addr+' -n 4', stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
		[out, error] = ping.communicate()
		output = out.decode()
		if not error:
			#ping_stats = re.search(r'.*Sent = (\d+),.*(\d+),.*(\d+)%' , output)
			c_reply = output.lower().count('ttl')
			c_timeout = output.lower().count('timed out')
			c_dest = output.lower().count('destination')
			#c_loss = int(ping_stats.group(3))
			self.ping_status.append({ip_addr:[c_reply,c_timeout,c_dest]})
			#print(ip_addr, c_reply, c_timeout, c_dest)
		else:
			print('ping command execution failed.Please verify')
			exit()

	def start_ping(self):
		'''
		function starts the simultaneous ping to the ip address in the list by creating thread objects.
		Then it wait till all the threads to complete their tasks.
		It will igonre the dummy threads which may exists.
		'''
		for i in self.ip_list:
			threading.Thread(target=self.ping_ip, args=(i,)).start()
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

	def check_ping_health(self):
		'''
		this function gives the percentage of successful pings
		rearranges in a order and then applies the formula to calculate health
		'''
		self.final_ping_status = []
		for i in self.ip_list:
			for j in self.ping_status:
				try :
					self.final_ping_status.append(j[i])
				except KeyError:
					pass
		for each in self.final_ping_status:
			self.ping_health.append(int((each[0]/4)*100))

	def windows_remote_check(self,ip_addr):
		'''
		this function verifies whether remote connection is enabled for the given ip address of windows machine
		appends the status(element format --> {ip:status}) to remote_conn_status list variable
		'''
		try:
			rdp_cmd = """If (New-Object System.Net.Sockets.TCPClient -ArgumentList """ + ip_addr + """,3389) { Write-Host 'RDP is open' }
			If ($? -eq $false) { Write-Host 'Something went wrong' }"""
			rdp_out = subprocess.Popen('powershell '+ rdp_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			[out, error] = rdp_out.communicate()
			rdp_status = out.decode()
		except:
			print('Unable to run powershell script of checking rdp connections')

		if 'RDP is open' in rdp_status:
			self.remote_conn_status.append({ip_addr : 'Success'})
		else:
			#print('A remote connection attempt failed to ',ip_addr)
			self.remote_conn_status.append({ip_addr :'Fail'})

	def start_windows_remote_check(self):
		'''
		function starts the simultaneous rdp check to the ip address in the list by creating thread objects.
		Then it wait till all the threads to complete their tasks.
		It will igonre the dummy threads which may exists.
		'''
		for i in self.ip_list_windows:
			threading.Thread(target=self.windows_remote_check, args=(i,)).start()
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

	def ssh_connect(self,ssh_params):
		'''
		ssh_params is the list object contains ip,user,password elements [ipaddresss, user, password]
		Tries ssh remote connection and appends the status(element format --> {ip:status}) to remote_conn_status list variable
		'''
		try:
		    ssh = paramiko.SSHClient()
		    warnings.filterwarnings(action='ignore',module='.*paramiko.*') # To eliminate display of warning statements w.r.t cryptography version used by paramiko module
		    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		    paramiko.util.log_to_file("Exception.log")
		    ssh.connect(ssh_params[0],username=ssh_params[1],password=ssh_params[2])
		    #print("Connected to", ssh_conn_list[0])
		    self.remote_conn_status.append({ssh_params[0] : 'Success'})
		except paramiko.AuthenticationException:
		    print("Failed to connect to" , ssh_conn_list[0] , "due to wrong username/password")
		    self.remote_conn_status.append({ssh_params[0] : 'Fail'})
		except Exception as e:
		    #print(e)
		    self.remote_conn_status.append({ssh_params[0] : 'Fail'}) 
		finally:
			if ssh: 
				ssh.close()

	def start_linux_remote_check(self):
		'''
		function starts the simultaneous ssh to the ip address in the list by creating thread objects.
		Then it wait till all the threads to complete their tasks.
		It will igonre the dummy threads which may exists.
		'''
		with open('Exception.log','w'): pass #just to clear the logs of previous run
		for i in self.ip_list_linux:
			threading.Thread(target=self.ssh_connect, args=(i,)).start()
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

	def get_remote_conn_status(self):
		'''
		this function does fetch remote status string from remote_conn_status and sort them as per ip_list 
		the strings are then appended to final_remote_conn_status
		'''
		for i in self.ip_list:
			for j in self.remote_conn_status:
				try :
					self.final_remote_conn_status.append(j[i])
				except KeyError:
					pass

	def create_csv(self):
		'''
		this function creates a csv file with ip_list, hostname , ping health and remote connectivity when called
		'''
		try:
			with open('hosts_status.csv', 'w') as new_file:
				print('started creating csv file for host status !!!')
				fieldnames = ['ip_address', 'host_name', 'ping_health', 'remote_conn_status']
				output_lines = tuple(map(lambda a,b,c,d: [a,b,c,d],self.ip_list, self.hosts_name, self.ping_health, self.final_remote_conn_status))
				csv_writer = csv.writer(new_file)
				csv_writer.writerow(fieldnames)
				for line in output_lines:
					csv_writer.writerow(line)
		except PermissionError:
			print("Permission denied: 'hosts_status.csv'. Close the file if already opened")
			exit()

	def send_email(self,list_files,list_contacts):
		'''
		This method will send the mail to list_contacts with attachments of list_files
		''' 
		email_address= 'pasupathi.thumburu@gmail.com'
		email_password = os.environ.get('EMAIL_PASSWORD')
		msg = EmailMessage()
		msg.set_content('Refer files attached...')
		msg['Subject'] = 'Current host status'
		msg['From'] = email_address
		msg['To'] = list_contacts
		files = list_files
		for file in files:
			with open(file, 'rb') as f:
				file_data = f.read()
				file_name = f.name
				msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

		with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
			try:
				smtp.login(email_address,email_password)
			except:
				print('Please check the email credentials. Seems got error while login or sendind an email')
			smtp.send_message(msg)

myInstance = Host_status()