# WAS accept a file and count total no.of records in a given file.

import sys

x=open(sys.argv[1],"r")
data=x.readlines()
print("Total no.of records : ",len(data))
x.close()
