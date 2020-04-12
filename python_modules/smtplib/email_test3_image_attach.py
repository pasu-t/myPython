import smtplib
import os
from email.message import EmailMessage
import imghdr

email_address= 'pasupathi.thumburu@gmail.com'
email_password = os.environ.get('EMAIL_PSWD')
msg = EmailMessage()
msg.set_content('Image attached...')
msg['Subject'] = 'Hey buddy check my well'
msg['From'] = email_address
msg['To'] = email_address
with open('mywell.jpg', 'rb') as f:
	file_data = f.read()
	file_type = imghdr.what(f.name)
	file_name = f.name
	msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_address,email_password)
	smtp.send_message(msg)
