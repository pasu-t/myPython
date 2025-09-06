import os
fn=input("Enter a filename : ")
if os.path.exists(fn) :
    if  os.path.isfile(fn) :
        
        str1=input("Enter a string to delete : ")
        with open(fn,"r") as x :
            data=x.read()
            
        if  str1 in data :
            data=data.replace(str1,"")
            with open(fn,"w") as x :
                x.write(data)
            print(str1,"word deleted from a ",fn,"file.")
        else :
            print(str1,"word not found in ",fn,"file.")
    else :
        print(fn,"is not a file")
else :
    print(fn,"no such file or directory")
#____________________________________________
# copy a file
import os
src=input("Enter a source filename : ")
if os.path.exists(src) and os.path.isfile(src) :
    trg=input("Enter a target filename  to copy : ")
    with open(src,"r") as x :
        data=x.read()  #  data=x.readlines()
    with  open(trg,"w") as x :
        x.write(data)  #  x.writelines(data)
    print("File copied successfully")
else :
    print("Copy failed.No such source file  ")

*******************************
### Happy Independence Day   ###
*******************************
