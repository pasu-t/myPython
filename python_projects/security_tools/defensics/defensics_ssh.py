import paramiko
import warnings
import re
import time


class Defensics:

	def __init__(self, defensics_dict):
		self.ssh = paramiko.SSHClient()
		try:
			self.host = defensics_dict['host']
			self.username = defensics_dict['username']
			self.password = defensics_dict['password']
			self.bootjar_folder = defensics_dict['bootjar_folder']
			self.testplan_folder = defensics_dict['testplan_folder']
			self.output_log_folder = defensics_dict['output_log_folder']
		except Exception as e:
			raise AssertionError(e)

	def open_connection(self):
		'''
		Log into the defensics server using SSH connection

        *Parameters:* None

        *Return:* None
		'''
		try:
		    warnings.filterwarnings(action='ignore',module='.*paramiko.*') # To eliminate display of warning statements w.r.t cryptography version used by paramiko module
		    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		    self.ssh.connect(self.host, username=self.username, password=self.password)
		    print("Connected to defensics server " + self.host + " using SSH protocol")
		except paramiko.AuthenticationException:
			raise AssertionError("Connection failed to " + self.host + " due to wrong username/password")
		except Exception as e:
		    raise AssertionError(e)

	def run_defensics_cmd(self, testplan):
		'''
		Initially removes the log file of previuos run if they were present in the folder
		This method does run the defensics test through command line and stores the command output in a log file

        *Parameters:* name of the testplan

        *Return:* None
		'''
		try:
			sftp_conn = self.ssh.open_sftp()
			# sftp_conn.remove('C:/Users/sherlock/synopsys/automation_log/' + testplan + '.log')
			sftp_conn.remove(self.output_log_folder + testplan + '.log')
			time.sleep(3)
			print('Removed log file of previous run')
		except IOError:
			print('Error: No such file to remove')
		except Exception as e:
			print(e)
		finally:
			sftp_conn.close()

		cmd = 'cd ' + self.bootjar_folder + ' && java -jar boot.jar --testplan ' + self.testplan_folder + testplan + '.testplan > ' + self.output_log_folder + testplan + '.log' 
		print("running the defensics command: " + cmd)
		
		try:
			stdin, stdout, stderr = self.ssh.exec_command(cmd)
			time.sleep(3)
			exit_status = stdout.channel.recv_exit_status() 
			if exit_status == 0:
				print ("############################ Command run successfully ##############################")
			else:
				print("Error", exit_status)
		except Exception as e:
		    raise AssertionError(e)

		# err = ''.join(stderr.readlines())
		# out = ''.join(stdout.readlines())
		# self.final_output = str(out)+str(err)
		# print(self.final_output)

	def get_final_result(self, testplan):
		'''
		This method just gets the statistics, status and final result of test suites run by defensics
		Also closes sftp connection and ssh connection to defensics server

        *Parameters:* name of the testplan

        *Return:* dictionary that contains result status and other statistics of test suite
		'''
		result_dict = {}
		# i = 0
		# while self.ssh is None:
		# 	time.sleep(2)
		# 	self.open_connection()
		# 	i += 1
		# 	if i > 5:
		# 		print('SSH connection to defensics is failing')
		# 		break
		try:
			sftp_conn = self.ssh.open_sftp()
			print('############## Reading the log file ##############')
			remote_file = sftp_conn.open(self.output_log_folder + testplan + '.log')
			print(remote_file.read())
			remote_file.seek(0)
			for line in remote_file:
				# print(line)
				var1 = re.search(r'.*MESSAGE:(Suite) (.*)\s*executed', line)
				var2 = re.search(r'.*MESSAGE:(Test run verdict):(.*)', line)
				var3 = re.search(r'.*\:(Executed cases:\d+)\s*(Passed:\d+)?\s*(Inconclusive cases:\d+)?\s*(Failed cases:\d+)?',line)
				var4 = re.search(r'.*MESSAGE:(Testplan) (\w+)', line)
				var5 = re.search(r'(.*(ERROR):(Suite:.*Licensed number of users already reached))', line)
				var6 = re.search(r'.*(ERROR):(Testplan loading failed).*', line)
				var7 = re.search(r'.*(ERROR):.*:(Error in initialization, unusable device or missing administrator rights).*', line)
				var8 = re.search(r'.*(ERROR):Suite.*(No license for suite).*(found).*', line)
				if var1:
					result_dict[var1.group(1)] = var1.group(2)
				elif var2:
					result_dict[var2.group(1)] = var2.group(2).rstrip()
				elif var3:
					result_dict[var3.group(1).split(':')[0]] = var3.group(1).split(':')[1]
					if var3.group(2):
						result_dict[var3.group(2).split(':')[0]] = var3.group(2).split(':')[1]
					if var3.group(3):
						result_dict[var3.group(3).split(':')[0]] = var3.group(3).split(':')[1]
					if var3.group(4):
						result_dict[var3.group(4).split(':')[0]] = var3.group(4).split(':')[1]
						print (result_dict)
						raise AssertionError('Vulnerabilties detected on the target.')
				elif var4:
					result_dict[var4.group(1) + ' execution status'] = var4.group(2)
				elif var5:
					raise AssertionError(var5.group(0))
				elif var6:
					raise AssertionError(var6.group(0))
				elif var7:
					raise AssertionError(var7.group(0) + ' Running testplan manually may help')
				elif var8:
					raise AssertionError(var8.group(0))
		except Exception as e:
			raise e
		finally:
			sftp_conn.close()
			print('-'*50)
			self.ssh.close()
			print('closed ssh connection to defensics server...')
			print('-'*50)

		if result_dict == {}:
			raise AssertionError('Unable to parse defensics results from the log file')
		return result_dict

if __name__ == '__main__':
	pass
	# ob = Defensics({'host': '10.49.20.226',
 #    'username' : 'sherlock', 
 #    'password' : 'Adtran1234',
 #    'output_log_folder' : 'C:/Users/sherlock/synopsys/automation_log/',
 #    'testplan_folder'   : 'C:/Users/sherlock/synopsys/defensics/testplans/',
 #    'bootjar_folder'    : 'C:/Program Files/Synopsys/Defensics/monitor',})
	# ob.open_connection()
	# ob.run_defensics_cmd('401_ARP-Server_Sample')
	# print(ob.get_final_result('401_ARP-Server_Sample'))
