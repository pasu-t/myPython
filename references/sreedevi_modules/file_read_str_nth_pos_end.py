#  Write a python script accept a file and string , if given string found
#then read data from given string to end of the file.

import os
fn=input("Enter a filename : ")
if  os.path.exists(fn) :
    if os.path.isfile(fn) :
        str1=input("Enter a string : ")
        with  open(fn,"r") as x :
            data=x.read()
        n=data.find(str1)
        if n>0 :
            print(data[n:])
        else :
            print(str1,"word not found in a file")
    else :
        print(fn,"is not a file")
1)Write a python script accept a file and count total no.of characters ,
total no of words and total no.of lines.

4) Write a python script and delete duplicate lines from a file.

5) Write a python script delete empty lines from a give file.

6) Write a python script accept a file and display each line last word.

7) write a python script accept a file and display file contents
in sorted order.

8) Write a python script accept file and reverse the file contents.

10) write a python script accept a file and diplay frequency
 of words in dictionary format.

11) Write a python script accept a file and string and count 
total no of occurences.

12) Write a python script create given no of directories in the
current directory. 

13) Write a python script to copy a file

14) Write a python script to move a file.

15) Write a python script accept 2 files and concatenate 2 files data and
store into 3rd file.

16) Write a python script accept a directory  and count total no.of files
 and total no.of directories.

17) Write a python script accept a directory and list which  file  are sizes
more than 1000 bytes.

18) Write a python script accept a directory and display only .py files
from a given directory

19) Write a python script accept a file and check the given file exist
in the current directory or not.

20) Write a python script accept 2 files and check whether 2 files same
or not if files are not same and display those lines from 2 files.














 












else:
    print(fn,"bno such file or directory")


#__________________________________________
# Write python script accept a directory and add the following messge
#at end of each file in a given directory.
#("All the best")

import os

dn=input("ENter a directory name : ")

if os.path.exists(dn) :
    if os.path.isdir(dn) :
        os.chdir(dn)
        print(os.getcwd())
        files=os.listdir(".")
        print(files)

        for  i  in  files :
            if os.path.isfile(i) :
                with  open(i,"a") as x :
                    x.write("\n *********************************** \n")
                    x.write(" ###  Happy Vinayakachavithi  ###")
                    x.write("\n *********************************** \n")
        print("Message updated successfully")
    else :
        print(dn,"is not a directory")
else :
    print(dn,"no such filr or directory")
                
                    
#_________________________________
    1)Write a python script accept a file and count total no.of characters ,
total no of words and total no.of lines.

4) Write a python script and delete duplicate lines from a file.

5) Write a python script delete empty lines from a give file.

6) Write a python script accept a file and display each line last word.

7) write a python script accept a file and display file contents
in sorted order.

8) Write a python script accept file and reverse the file contents.

10) write a python script accept a file and diplay frequency
 of words in dictionary format.

11) Write a python script accept a file and string and count 
total no of occurences.

12) Write a python script create given no of directories in the
current directory. 

13) Write a python script to copy a file

14) Write a python script to move a file.

15) Write a python script accept 2 files and concatenate 2 files data and
store into 3rd file.

16) Write a python script accept a directory  and count total no.of files
 and total no.of directories.

17) Write a python script accept a directory and list which  file  are sizes
more than 1000 bytes.

18) Write a python script accept a directory and display only .py files
from a given directory

19) Write a python script accept a file and check the given file exist
in the current directory or not.

20) Write a python script accept 2 files and check whether 2 files same
or not if files are not same and display those lines from 2 files.














 


























        
        



















