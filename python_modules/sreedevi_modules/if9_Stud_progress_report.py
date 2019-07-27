'''
WAP accept student name,and three subject marks
 and calculate total marks,avg marks,result, and grade
 based  on following conditions

 NOTE : pass marks is 40
 avg marks      grade
 >=90           A+
 >=80 and <90   A
 >=70 and <80   B
 >=60 and <70   C
 >=50 and <60   D
 <50            E
'''

sname=input("Enter student name : ")
m1=int(input("Enter marks 1 : "))
m2=int(input("Enter marks 2 : "))
m3=int(input("Enter marks 3 : "))

total_marks=m1+m2+m3
avg_marks=total_marks/3

if  m1>=40  and  m2>=40  and m3>=40 :
    result="PASS"
else :
    result="FAIL"

if result=="PASS" :
    if avg_marks>=90 : grade="A+"
    elif avg_marks>=80 : grade="A"
    elif avg_marks>=70 : grade="B"
    elif avg_marks>=60 : grade="C"
    elif avg_marks>=50 : grade="D"
    else : grade="E"
else :
    grade="_"

print("\t\t Student  Progress Report ")
print("-" * 50)
print("\t Student name     :  ",sname)
print("\t Subject1 marks   :  ",m1)
print("\t Subject2 marks   :  ",m2)
print("\t Subject3 marks   :  ",m3)
print("\n\t Result          :  ",result)
print("\t Total Marks       :  ",total_marks)
print("\t AVG Marks         :  ",avg_marks)
print("\t Grade             :  ",grade)
print("-" * 50)





