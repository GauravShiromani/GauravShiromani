# write a program to calculate grade of a student 
# from his marks from the following scheme 
    # 90  -  100  ex
    # 80  -  90   A
    # 70  -  80   B
    # 60  -  70   C
    # 50  -  60   D
        # <  50   F


marks = input("enter your marks")

if marks  >= 90 :
    print("excilent")
if marks >= 80 :
    print("A")
if marks >= 70 :
    print("B")
if marks >= 60 :
    print("c")            
if marks >= 50 :
    print("d")
if marks < 50 :
    print ("F")

print(marks)