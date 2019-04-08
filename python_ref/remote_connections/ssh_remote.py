import paramiko
ip='test.rebex.net'
port=22
username = 'demo' 
password = 'password'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(ip,port,username,password)
stdin,stdout,stderr=ssh.exec_command('ls')
outlines=stdout.readlines()
resp=''.join(outlines)
print(resp)