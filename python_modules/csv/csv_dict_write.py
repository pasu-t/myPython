import csv
with open('hosts.csv', 'r') as file:
	csv_reader = csv.DictReader(file)
	print(csv_reader)

	with open('new_hosts.csv', 'w') as new_file:
		fieldnames = ['ip_address','host_name','os','conn_protocol','user','password']
		csv_writer = csv.DictWriter(new_file, fieldnames)
		csv_writer.writeheader()
		for line in csv_reader:
			csv_writer.writerow(line)