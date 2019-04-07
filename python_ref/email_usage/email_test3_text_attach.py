import smtplib
import os
from email.message import EmailMessage
import imghdr

email_address= 'pasupathi.thumburu@gmail.com'
email_password = os.environ.get('EMAIL_PSWD')
msg = EmailMessage()
msg.set_content('Files attached...')
msg['Subject'] = 'Hey buddy check my files'
msg['From'] = email_address
msg['To'] = email_address
files = ['sample.txt']
for file in files:
	with open(file, 'rb') as f:
		file_data = f.read()
		file_name = f.name
		msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_address,email_password)
	smtp.send_message(msg)
