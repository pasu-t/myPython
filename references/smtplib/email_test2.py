import smtplib
import os
from email.message import EmailMessage
email_address= 'pasupathi.thumburu@gmail.com'
email_password = os.environ.get('EMAIL_PSWD')
msg = EmailMessage()
msg['Subject'] = 'Hello dude'
msg['From'] = email_address
msg['To'] = email_address
msg.set_content('Lets rock again')
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
	smtp.login(email_address,email_password)
	smtp.send_message(msg)
