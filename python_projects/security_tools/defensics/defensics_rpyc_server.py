import rpyc
import subprocess
import re

class MyService(rpyc.Service):
    def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
        # print(conn._config['sync_request_timeout'])
        print("rpyc service connected")
        pass

    def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
        print("rpyc service disonnected")
        pass

    def exposed_run_defensics_cmd_s(self, testplan):
        """
        netstat -ano | findstr :18861
        taskkill /PID 6048 /F
        """
        cmd = 'java -jar boot.jar --testplan C:/Users/sherlock/synopsys/defensics/testplans/' + testplan + '.testplan'
        log_dir = ' > C:/Users/sherlock/synopsys/automation_log/' + testplan + '.log'

        try:
           return subprocess.check_output('cd C:/Program Files/Synopsys/Defensics/monitor && '+ cmd + log_dir, shell = True)

        except subprocess.CalledProcessError as e:
            if 'returned non-zero exit status 1' in e:
                return None

        except Exception as e2:
            return e2

        # try:
        #     subprocess.check_call('cd C:/Program Files/Synopsys/Defensics/monitor && '+ cmd + log_dir, shell = True)
        # except Exception as e:
        #     print('******************** defensics command execution failed **********************')
        #     return e
        # print("##################### Defensics command run successfully ##########################")
        # return True

    def exposed_get_defensics_results_s(self, testplan):
        """
        Reads the log file run by defensics command and resurns the results 
        """
        result_dict = {}
        log_path = "C:/Users/sherlock/synopsys/automation_log/" + testplan + ".log"
        try:
            with open(log_path) as f:
                for line in f:
                    var1 = re.search(r'.*MESSAGE:(Suite) (.*) \s*executed', line)
                    var2 = re.search(r'.*MESSAGE:(Test run verdict):(.*)', line)
                    var3 = re.search(r'.*MESSAGE:(Executed cases):(\d+).*(Passed):(\d+).?((Failed cases):(\d+))?', line)
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
                        result_dict[var3.group(1)] = int(var3.group(2))
                        result_dict[var3.group(3)] = int(var3.group(4))
                        if var3.group(5):
                            result_dict[var3.group(6)] = int(var3.group(7))
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
            return e
        if result_dict == {}:
            return AssertionError('Unable to parse defensics results from the log file')
        return result_dict

	def get_question(self):
		return "still not done??"

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861, protocol_config = {'allow_public_attrs':True})
    t.start()