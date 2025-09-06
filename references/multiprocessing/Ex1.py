# import multiprocessing
import concurrent.futures
import time

def do_something(seconds):
	print(f'sleeping {seconds} second(s)....')
	time.sleep(seconds)
	return f'done sleeping {seconds} second(s).....'

if __name__ == '__main__':
	
	start = time.perf_counter()

	with concurrent.futures.ProcessPoolExecutor() as executor:
		secs = [5,4,3,2,1]
		results = executor.map(do_something, secs)
		for result in results:
			print(result)

	# with concurrent.futures.ProcessPoolExecutor() as executor:
	# 	results = [executor.submit(do_something, 1) for _ in range(10)]
	# 	for f in concurrent.futures.as_completed(results):
	# 		print(f.result())

	# processes = []

	# for _ in range(10):
	# 	p = multiprocessing.Process(target = do_something, args = [1])
	# 	p.start()
	# 	processes.append(p)

	# for process in processes:
	# 	process.join()

	finish = time.perf_counter()
	print(f'Finished in {round(finish-start, 2)} second(s)')
