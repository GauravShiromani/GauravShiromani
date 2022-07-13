# write a program to find out wheather a student is pass or fail , if
# it requid totle 40% amnd atleast 33% in each subject to pass assume 3 subject and take marks 
# as an input from the user 


m1 = int(input("enter your marks for subject 1: "))
m2 = int(input("enter your marks for subject 2: "))
m3 = int(input("enter your marks for subject 3: "))

overAll = (m1+m2+m3)/3

if (overAll >= 40):
    if(m1>=33 and m2>=33 and m3>=33):
     print("you have pass the exam")
    else:
        print("you have not passed the exam due to one of the subject")
else: 
     print("you have not passed the exam due to over all percentage")
