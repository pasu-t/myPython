import subprocess
if 0:
	p1 = subprocess.run(['ipconfig', '/all'], shell=True)
	print(p1)
	print(p1.args)
	print(p1.returncode)
	print(p1.stdout)
if 0:
	p2 = subprocess.run("dir",capture_output=True, shell=True)
	print(p2.stdout)
if 0:
	p3 = subprocess.run("dir",capture_output=True, shell=True)
	print(p3.stdout.decode())

if 0:
	p4 = subprocess.run("dir",capture_output=True, shell=True, text=True)
	print(p4.stdout)
if 0:
	p5 = subprocess.run("dir", shell=True, stdout = subprocess.PIPE, text=True)
	print(p5.stdout)

if 0:
	with open("output.txt", "w") as f:
		subprocess.run("dir", shell = True, stdout = f, text = True )

if 0:
	p6 = subprocess.run(['ipconfiggg', ' /all'], shell=True, capture_output=True, text=True)
	print(p6.returncode)
	print(p6.stderr)
	if p6.returncode == 0:
		print("Command run successfully")
	else:
		print("Command failed to run")
if 0:
	p7 = subprocess.run(['ipconfiggg', ' /all'], shell=True, capture_output=True, text=True,check=True)

if 1:
	p8 = subprocess.run(['ipconfiggg', ' /all'], shell=True, stderr= subprocess.DEVNULL)
	print(p8.stderr)




