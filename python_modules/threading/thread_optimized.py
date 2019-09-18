import concurrent.futures
import time

start = time.perf_counter()

def do_something(seconds):
	print(f'sleeping {seconds} second(s)....')
	time.sleep(seconds)
	return f'done sleeping {seconds} second(s)....'

with concurrent.futures.ThreadPoolExecutor() as executor:
	secs = [5,4,3,2,1]
	# results = [executor.submit(do_something, 1) for _ in range(10)]
	results = [executor.submit(do_something, sec) for sec in secs]

	for f in concurrent.futures.as_completed(results):
		print(f.result())


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
