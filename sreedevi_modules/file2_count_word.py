# WAS accept a file and a string and count how many times
# the given string repeated in the file.

fn=input("Enter a filename : ") # a1.txt
str1=input("Enter a string : ") # python

with open(fn,"r") as x :
    data=x.read()
    cnt=data.count(str1)
print(str1,"word found",cnt,"times in a",fn,"file")

#___________________________________________
#WAS accept a file and a string and delete given string from a given
# file

fn=input("Enter a filename : ") # a1.txt
str1=input("Enter a string to delete : ") # python
with open(fn,"r") as x :
     data=x.read()

if  str1 in data :
    data=data.replace(str1,"")
    #print(data)
    with open(fn,"w") as x :
        x.write(data)
    print(str1,"word delete from a ",fn,"file.")
else :
    print(str1,"word not found in  a ",fn,"file.")
    
#_________________________________________
    OS module methods
------------------
systax  : os.methodname()

1. os.getcwd()
2. os.listdir("dirname")
3. os.mkdir("dirname")
4. os.chdir("dirname")
5. os.rmdir("dirname")
6. os.remove("filename")
7. os.rename("oldfile","newfile")
8. os.path.isfile("filename")
9. os.path.isdir("filename")
10. os.path.exists("filename")
11. os.path.isabs("filename")
12. os.path.getsize("filename")
13. os.path.basename("filename")
14. os.path.dirname("filename")
15. os.system("os commnad name")













     
