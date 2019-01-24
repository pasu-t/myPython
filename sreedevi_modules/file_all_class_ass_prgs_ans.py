# Write a python script accept a file and count total no.of characters ,
# total no of words and total no.of lines.

import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        lines=len(data) # counts no of lines
        x.seek(0,2)
        chars=x.tell() # counts no of characters

# counts bo of words
    words=0
    for i in data :
        w=i.split(" ")
        words=words+len(w)

    print "Total no.of lines : ",lines
    print "Total no of words : ",words
    print "Total no.of chars : ",chars
else :
    print fn,"file doesn't exist"
______________________________________________
#write a python script aceept a file and a string and delete the string
#from a file.

import os

fn=raw_input("Enter a filename : ")
str=raw_input("Enter a string : ")
if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.read()
        k=data.replace(str,"") # it deletes given string
    with open(fn,"w") as x :
        x.write(k)
else :
    print fn," file doesn't exist"
________________________________
# Write a python script accept a file and string , if given string found
#then read data from given string to end of the file.

import os

fn=raw_input("Enter a filename : ")
str=raw_input("Enter a string : ")
if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.read()
        k=data.find(str)
        if k>=0 :
            print data[k:]
        else :
            print str," string not found in the given file"
else :
    print fn," file doesn't exist"
__________________________________________
#Write a python script and delete duplicate lines from a file.
import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        data=list(set(data)) # Diplicate lines eliminated
    with open(fn,"w") as x :
        for i in data :
            x.write(i)

else :
    print fn," file doesn't exist"
____________________________________
#Write a python script delete empty lines from a give file.
import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        text=""
        for i in data :
            if i!="\n" :  # eleminates new line character
                text=text+i
    with open(fn,"w") as x :
        x.write(text)
       
else :
    print fn," file doesn't exist"
_______________________
#Write a python script accept a file and display each line last word.

import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        for i in data :
            k=i.split(" ")
            print k[-1]
               
else :
    print fn," file doesn't exist"
_____________________________________
# write a python script accept a file and display file contents
# in sorted order.

import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        data.sort() # it sorts the file contents
    with open(fn,"w") as x :
        for i in data :
            x.write(i)
               
else :
    print fn," file doesn't exist"
___________________________________
#Write a python script accept file and reverse the file contents.

import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.readlines()
        data.reverse() # it reverse the file contents
    with open(fn,"w") as x :
        for i in data :
            x.write(i)
               
else :
    print fn," file doesn't exist"
____________________________________
#Write python script accept a directory and add the following messge
#at end of each file in a given directory.
#("Happy New Year 2018")

import os

dn=raw_input("Enter a directoryname : ")

if  os.path.exists(dn)  and  os.path.isdir(dn) :
    os.chdir(dn)
    files=os.listdir(".")
    print files
    for i in files :
        with open(i,"a") as x:
            x.write("\n ******************* \n")
            x.write(" ###   Happy New Year 2018 ### ")
            x.write("\n ******************* \n")
            
else :
    print dn," directory doesn't exist"
_________________________________________

________________________________
#Write a python script accept a file and string and count 
#total no of occurences.
import os

fn=raw_input("Enter a filename : ")
str=raw_input("Enter a string : ")
if  os.path.exists(fn)  and  os.path.isfile(fn) :
    with open(fn,"r") as x :
        data=x.read()
        k=data.count(str)
        print str," string occured",k,"times in a file"
else :
    print fn," file doesn't exist"
__________________________________
#Write a python script create given no of directories in the
#current directory.

import os
n=input("Enter no.of directories u want to create : ")

for i in range(1,n+1) :
    dn="abc"+str(i)
    os.mkdir(dn)
print n,"directories are created"
___________________________

# Write a python script to copy a file
import os
fn1=raw_input("Enter a source filename : ")
fn2=raw_input("Enter a target filename : ")
if  os.path.exists(fn1)  and  os.path.isfile(fn1) :
    with open(fn1,"r") as x :
        data=x.read()
    with open(fn2,"w") as x :
        x.write(data)
    print "File copied successfully"

else :
    print fn," source file doesn't exist.copy failed"
_____________________________________
# Write a python script to move a file.
import os
fn1=raw_input("Enter a source filename : ")
fn2=raw_input("Enter a target filename : ")
if  os.path.exists(fn1)  and  os.path.isfile(fn1) :
    with open(fn1,"r") as x :
        data=x.read()
    with open(fn2,"w") as x :
        x.write(data)
    os.remove(fn1)
    print "File moved successfully"

else :
    print fn," source file doesn't exist.move failed"
___________________________________________________
# Write a python script accept 2 files and concatenate 2 files data and
#store into 3rd file.
import os
fn1=raw_input("Enter a  filename1 : ")
fn2=raw_input("Enter a  filename2 : ")
fn3=raw_input("Enter a filename3 to write data : ")
if  os.path.exists(fn1)  and  os.path.isfile(fn1) :
    if  os.path.exists(fn2)  and  os.path.isfile(fn2) :
        with open(fn1,"r") as x :
            file_data1=x.read()
        with open(fn2,"r") as x :
            file_data2=x.read()
        data=file_data1+"\n"+file_data2
        with open(fn3,"w") as x :
            x.write(data)
        print "Successfully written file1 and file2 data ino file3"
    else :
        print fn2," file2 doen't exist"
else :
    print fn1," file1 doesn't exist"
___________________________________________
#Write a python script accept a directory  and count total no.of files
#and total no.of directories.

import os

dn=raw_input("Enter a directoryname : ")

if  os.path.exists(dn)  and  os.path.isdir(dn) :
    os.chdir(dn)
    files=os.listdir(".")
    fcnt=0
    dcnt=0
    for i in files :
        if os.path.isfile(i) : fcnt+=1
        elif os.path.isdir(i) : dcnt+=1
    print "Total files : ",fcnt
    print "Total directories : ",dcnt
            
else :
    print dn," directory doesn't exist"

__________________________________________
#Write a python script accept a directory and list which are file sizes
#more than 1000 bytes

import os

dn=raw_input("Enter a directoryname : ")

if  os.path.exists(dn)  and  os.path.isdir(dn) :
    os.chdir(dn)
    files=os.listdir(".")
    for i in files :
        x=os.path.getsize(i)
        if x>1000 :
            print i, "size : ",x
            
else :
    print dn," directory doesn't exist"

____________________________________
#Write a python script accept a directory and display only .py files
#from a given directory

import os

dn=raw_input("Enter a directoryname : ")

if  os.path.exists(dn)  and  os.path.isdir(dn) :
    os.chdir(dn)
    files=os.listdir(".")
    for i in files :
        x=i.split(".")
        if x[-1]=="py":
            print  i
            
else :
    print dn," directory doesn't exist"

__________________________________
#Write a python script accept a file and check the given file exist
#in the current directory or not.
import os

fn=raw_input("Enter a filename : ")

if  os.path.exists(fn)  and  os.path.isfile(fn) :
    print fn,"File exist"
            
else :
    print fn," file doesn't exist"



