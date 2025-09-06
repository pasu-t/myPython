import nmap
# initialize the port scanner
nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
nmScan.scan('127.0.0.1', '21-443')
nmScan.scan('192.168.0.1', '21-443')

# run a loop to print all the found result about the ports
for host in nmScan.all_hosts():
    print(f'nmap command: {nmScan.command_line()}')
    print(f'Host : {host} ({nmScan[host].hostname()})')
    print(f'State : {nmScan[host].state()}')
    for proto in nmScan[host].all_protocols():
        print('----------')
        print(f'Protocol : {proto}')

    lport = nmScan[host][proto].keys()
     # lport.sort()
    for port in lport:
        print (f"port : {port}\tstate : {nmScan[host][proto][port]['state']}")
    print()
