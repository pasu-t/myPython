class x:
	def __init__(self):
		print('I am inside cuntsructor of x',self)
	def m1(self):
		print('I am inside m1 of x')
	def __del__(self):
		print('I am inside destructor of x', self)
x1 = x()
print('#'*50)
x2 = x1
print('#'*50)
x3 = x2
print('#'*50)
x1 = x()
print('#'*50)
x2 = x()
print('#'*50)
x3 = x()
print('#'*50)