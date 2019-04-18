import paramiko
ip='10.49.20.152'
port=22
username = 'root' 
password = 'adtran1234'
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys(None)
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command('ls')
if stdout:
	outlines=stdout.readlines()
	resp=''.join(outlines)
	print(resp)
else:
	print(stderr)


