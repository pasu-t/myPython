import os

file_path = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
with open(file_path, 'w') as f:
    f.write('something')

print(os.path.exists('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))
print(os.path.isfile('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))
print(os.path.isdir('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))

print(os.path.basename('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))
print(os.path.dirname('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))
print(os.path.split('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))
print(os.path.splitext('C:\\workspace\\myPython\\python_modules\\os\\most_used.py'))