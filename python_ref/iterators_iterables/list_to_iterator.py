num = [1,2,3]
#print(dir(num))
i_num = iter(num) #same as i_num = num.__iter__()
#print(dir(i_num))
# print(next(i_num))
# print(next(i_num))
# print(next(i_num))
#print(next(i_num))
while True:
	try:
		print(next(i_num))
	except StopIteration:
		break


