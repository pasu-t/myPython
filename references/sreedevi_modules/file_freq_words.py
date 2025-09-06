#write a python script accept a file and diplay frequency
#of words in dictionary format.
import os

fn=input("Enter a filename : ")
if  os.path.exists(fn) :
    if os.path.isfile(fn) :
        with open(fn,"r") as x :
            data=x.read()
        #print(data)
        data=data.rstrip("\n").replace("\n"," ")
        words=data.split(" ")
        print(words)
        d1={}
        for  i  in  set(words) :
            cnt=words.count(i)
            d1[i]=cnt
        print(d1)
    else :
        print(fn,"is not a file")
else :
    print(fn,"no such file or directory")
        
