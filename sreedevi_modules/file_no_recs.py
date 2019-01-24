# WAS accept a file and count total no.of records in a given file.

fn=input("Enter a filename : ")
x=open(fn,"r")
data=x.readlines()
print("Total no.of records : ",len(data))
x.close()
