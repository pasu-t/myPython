import csv
with open('hosts.csv', 'r') as hosts_file:
	hosts_reader = csv.DictReader(hosts_file)
	print(type(hosts_reader))
	for line in hosts_reader:
		print(line)