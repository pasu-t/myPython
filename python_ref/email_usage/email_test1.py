import smtplib
import os
email_address= 'pasupathi.thumburu@gmail.com'
email_password = os.environ.get('EMAIL_PSWD')
#with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.ehlo()
	smtp.login(email_address,email_password)
	subject = 'Hello my dear!'
	body = "Let's have party tonight"
	msg = f'Subject: {subject}\n\n{body}'
	smtp.sendmail(email_address,email_address,msg)
