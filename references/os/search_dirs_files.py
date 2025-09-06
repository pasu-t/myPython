import os

for dirpath, dirnames, filenames in os.walk('C:\\workspace\\myPython\\python_modules'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)
    print()
