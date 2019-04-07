import csv
with open('hosts.csv', 'r') as file:
	csv_reader =csv.reader(file)
	for line in csv_reader:
		print(line)
