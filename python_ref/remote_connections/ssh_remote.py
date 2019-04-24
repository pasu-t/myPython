import paramiko
import warnings
linux_remote_check = []

def ssh_connect(host, username, password):
	try:
	    ssh = paramiko.SSHClient()
	    warnings.filterwarnings(action='ignore',module='.*paramiko.*') # To eliminate display of warning statements w.r.t cryptography version used by paramiko module
	    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	    ssh.connect(host,username=username,password=password)
	    print("Connected to", host)
	    linux_remote_check.append({host : 'Success'})
	except paramiko.AuthenticationException:
	    print("Failed to connect to" , host , "due to wrong username/password")
	    linux_remote_check.append({host : 'Fail'})
	    #exit(1)
	except Exception as e:
	    print(e)
	    linux_remote_check.append({host : 'Fail'})   
	    #exit(2)

def ssh_cmd_exec():
	try:
	    stdin, stdout, stderr = ssh.exec_command(cmd)
	except Exception as e:
	    print(e)

	err = ''.join(stderr.readlines())
	out = ''.join(stdout.readlines())
	final_output = str(out)+str(err)
	print(final_output)

#ssh_connect("10.49.20.152", "root","adtran1234" )
#ssh_connect("10.49.61.125", "admin1","adtran9638000")
#ssh_connect("10.49.61.125", "admin1","adtran9638000")
ssh_connect("10.49.8.64","adtran","adtran123")
print(linux_remote_check) #wrong credentials


