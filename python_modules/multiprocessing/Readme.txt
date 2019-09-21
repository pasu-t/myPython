Refer threading module once.
-> multiprocess is more of cpu bound operations than i/o bound. Threads are useful for i/o bound operations.
-> Try to experiment with threadpool and processpool and then decide the executor
-> Whenever you add more items, processes gives better performance than threads.
-> These pool executors are very useful in data science