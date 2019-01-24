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
