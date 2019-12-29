import rpyc


class DefensicsRPyC:

    def __init__(self, defensics_host="10.49.20.226", rpyc_port=18861):

        self.defensics_host = defensics_host
        self.rpyc_port = rpyc_port
        self.conn_obj = None

    def connect_defensics(self):
        """
        """
        try:
            self.conn_obj = rpyc.connect(self.defensics_host, self.rpyc_port)
            print("Connected to defensics server using rpyc")
        except Exception as e:
            raise AssertionError(e)

    def run_defensics_cmd(self, testplan):
        """
        """
        print("Running the defensics suite: " + testplan)
        cmd_status = self.conn_obj.root.run_defensics_cmd_s(testplan)
        # print("Status returned by subprocess.check_output: ")
        # print(cmd_status)

    def get_defensics_results(self, testplan):
        """
        """
        result = None
        result = self.conn_obj.root.get_defensics_results_s(testplan)
        # import pdb
        # pdb.set_trace()
        if isinstance(result, dict):
            if 'Failed cases' in result.keys():
                print (result)
                raise AssertionError('Vulnerabilties detected on the target.')
            return result
        else:
            raise AssertionError(result)


if __name__ == "__main__":
    ob1 = defensics()
    ob1.connect_defensics()
    # ob1.run_defensics_cmd('401_ARP-Server_Sample')
    print(ob1.get_defensics_results('401_ARP-Server_Sample'))
    # ob1.run_defensics_cmd('401_IPv4')
    # print(ob1.get_defensics_results('401_IPv4'))
