import csv
with open('hosts.csv', 'r') as hosts_file:
	hosts_reader = csv.DictReader(hosts_file)
	for line in hosts_reader:
		print(line['ip_address'],line['user'], line['password'])