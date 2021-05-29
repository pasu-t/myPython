from memory_profiler import memory_usage
import random
import time

names = ['pap', 'temp', 'chris', 'gold', 'cute', 'sema']
majors = ['Math', 'Eng', 'CmpSci', 'Arts', 'Business']

# print(help(memory_usage))

print('Memory Before: {} Mb'.format(memory_usage()[0]))

def people_list(num_people):
	result = []
	for i in range(num_people):
		person = {
					'id' : 1,
					'name': random.choice(names),
					'major': random.choice(majors),
		}
		result.append(person)
	return result

def people_generator(num_people):
	for i in range(num_people):
		person = {
					'id' : 1,
					'name': random.choice(names),
					'major': random.choice(majors),
		}
		yield person

t1 = time.perf_counter()
people = people_list(1000000)
t2 = time.perf_counter()

# t1 = time.perf_counter()
# people = people_generator(1000000)
# t2 = time.perf_counter()

print('Memory After: {} Mb'.format(memory_usage()[0]))
print('Took {} seconds'.format(t2-t1))




