import csv
import threading
import subprocess
import os
import re
import time
import smtplib
from email.message import EmailMessage

#Gobal variables
list_contacts = ['pasupathi.thumburu@gmail.com', 'malleswari.ysn@gmail.com']
list_files = ['hosts_status.csv']
ip_list = []
hosts_name = []
ping_status = []
ping_health = []
#remote_conn_check = []

#path = 'C:\\Users\\Home\\Desktop\\pasi\\python_ref\\csv_operations\\hosts.csv'

with open('hosts.csv', 'r') as hosts_file:
	hosts_reader = csv.DictReader(hosts_file)
	for line in hosts_reader:
		ip_list.append(line['ip_address'])
		hosts_name.append(line['host_name'])
	remote_conn_check = [' ' for _ in range(len(ip_list))]
	
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
		ping_status.append({ip_addr:[c_reply,c_timeout,c_dest]})
		# print(c_reply, c_timeout, c_dest)
	else:
		print('please check the given input')
		exit()
# for i in ip_list:
# 	ping_ip(i)
def start_ping():
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

def check_ping_health():
	for each in ping_status:
		for value in each.values():
			ping_health.append(int((value[0]/4)*100))

def create_csv():
	'''
	this function creates a csv file with ip_list, hostname , ping health and remote connectivity when called
	'''
	print('started creating csv file for host status !!!')
	with open('hosts_status.csv', 'w') as new_file:
		fieldnames = ['ip_address', 'host_name', 'ping_health', 'remote_conn_check']
		output_lines = tuple(map(lambda a,b,c,d: [a,b,c,d],ip_list, hosts_name, ping_health, remote_conn_check))
		csv_writer = csv.writer(new_file)
		csv_writer.writerow(fieldnames)
		for line in output_lines:
			csv_writer.writerow(line)
			# print(line)
def send_email(list_files,list_contacts):
	'''
	This method will send the mail to list_contacts with attachments of list_files
	''' 
	#contacts = ['pasupathi.thumburu@gmail.com']
	email_address= 'pasupathi.thumburu@gmail.com'
	email_password = os.environ.get('EMAIL_PSWD')
	msg = EmailMessage()
	msg.set_content('Files attached...')
	msg['Subject'] = 'Hey buddy check my files'
	msg['From'] = email_address
	msg['To'] = list_contacts
	files = list_files
	for file in files:
		with open(file, 'rb') as f:
			file_data = f.read()
			file_name = f.name
			msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(email_address,email_password)
		smtp.send_message(msg)

start_ping()
check_ping_health()
create_csv()
send_email(list_files,list_contacts)


