from telnetlib import Telnet
user = 'admin' 
pswd = 'adtran9638000'
try:
	with Telnet('10.49.61.180', 23) as tn:
		try:
			tn.read_until(b"Login: ", 5)
			tn.write(user.encode('ascii') + b"\n")
			tn.read_until(b"Password: ", 5)
			print('connected')
			tn.write(pswd.encode('ascii') + b"\n")
		except EOFError:
			print ("Authentication failed.\n")
except ConnectionRefusedError:
	print('Target device refused the telnet connection request')
	exit()

