import csv
from multiping import multi_ping
import smtplib
from email.message import EmailMessage

class network_monitor():

	notify_list = ['pasupathi.thumburu@gmail.com', 'bluefrog.pashu@gmail.com']

	def __init__(self):

		self.ip_list = []
		self.hosts_name = []
		self.ping_fail_ip = []
		try:
			with open('hosts.csv', 'r') as hosts_file:
				hosts_reader = csv.DictReader(hosts_file)
				for line in hosts_reader:
					self.ip_list.append(line['ip_address'])
					self.hosts_name.append(line['host_name'])
		except FileNotFoundError:
			print('hosts.csv file is not found.Please check.')


	def check_ping(self):
		'''
		Ping the addresses up to 4 times (initial ping + 3 retries), over the
		course of 2 seconds. This means that for those addresses that do not
		respond another ping will be sent every 0.5 seconds.
		'''
		addrs = ["192.168.0.1", "192.168.0.100", "192.168.0.2", "192.168.0.102", "192.168.0.101"]
		responses, no_responses = multi_ping(addrs, timeout=3, retry=3)
		for addr, rtt in responses.items():
		    print(f"{addr} responded in {rtt} seconds")
		self.ping_fail_ip = no_responses

	def send_email(self):
		'''
		This method will send the mail to list_contacts with attachments of list_files
		''' 
		if self.ping_fail_ip:

			email_body = "Ping Failure IP's\n"
			for ip in self.ping_fail_ip:
				email_body += ip + '\n'
			email_address= 'test.pasupathi@gmail.com'
			email_password = 'test@321'
			msg = EmailMessage()
			msg.set_content(email_body)
			msg['Subject'] = "Warning! Network Ping Failure"
			msg['From'] = email_address
			msg['To'] = network_monitor.notify_list

			with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
				try:
					smtp.login(email_address,email_password)
				except:
					print('Check the credentials or server settings. Seen error while login or sendind an email')
				smtp.send_message(msg)

if __name__ == '__main__':
	monitor = network_monitor()
	monitor.check_ping()
	monitor.send_email()