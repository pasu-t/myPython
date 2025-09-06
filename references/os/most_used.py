import os
from datetime import datetime

cwd = os.getcwd()
print(cwd)
os.chdir('C:\\workspace\\myPython\\python_modules')
print(os.getcwd())
print(os.listdir())
os.chdir(cwd)
print(os.listdir())
os.mkdir('test')
os.rmdir('test')
os.makedirs('test\\sub')
os.removedirs('test\\sub')
os.rename('test.txt', 'test1.txt')
print(os.stat('test1.txt'))
os.rename('test1.txt', 'test.txt')
print(os.stat('test.txt').st_size)
mod_time = os.stat('test.txt').st_mtime
print(datetime.fromtimestamp(mod_time))