import smtplib
'''
use debug server with python command:
python -m smtpd -c DebuggingServer -n localhost:1025
The mails will not be sent to destination mail instead to local terminal where server is running
'''
email_address= 'pasupathi.thumburu@gmail.com'
email_password = ''
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
with smtplib.SMTP('localhost', 1025) as smtp:
	# smtp.ehlo()
	# smtp.starttls()
	# smtp.ehlo()
	# smtp.login(email_address,email_password)
	subject = 'Hello my dear!'
	body = "Let's have party tonight"
	msg = f'Subject: {subject}\n\n{body}'
	smtp.sendmail(email_address,email_address,msg)
