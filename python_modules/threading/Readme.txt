-> Threading doesn't run the code same time. 
-> As soon as function/thread starts waiting, another function/thread will start running. These two are overlapped here.
-> We never actually run the of the code at the same time. It just creates an illusion of running the code at same time.
-> In python 3.2 they added thread pool executor and in lot of cases this to be an easier and more efficient way to run these threads.It also allows us to switch to multiple processes instead of threads as well depending on the problem that we're trying to solve

-> When we use map method instead if submit method , it will return the results instead of future object in the order the threads started. It still takes the same time as submit method.

-> If our function raises the exception, it won't actually rise the exception while running the thread. Exception will be raised when its value is retrieved from the result iterator. You need to handle exception inside the iterator.
