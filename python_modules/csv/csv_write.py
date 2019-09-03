import csv
dir(csv)
with open('hosts.csv', 'r') as file:
	csv_reader =csv.reader(file)
	# for line in csv_reader:
	# 	print(line)
	with open('new_hosts.csv', 'w', newline='') as new_file:
		csv_writer = csv.writer(new_file, delimiter='-')
		for line in csv_reader:
			csv_writer.writerow(line)
# with open('new_hosts.csv', 'r') as new_f:
# 	csv_r = csv.reader(new_f, delimiter='-')
# 	for line in csv_r:
# 		print(line)
