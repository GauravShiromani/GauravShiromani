#  write a program to accept marks of 6 students and display them in a shorted manner  
 
marks1 = int(input("enter marks of student1: "))

marks2 = int(input("enter marks of student2: "))

marks3 = int(input("enter marks of student3: "))

marks4 = int(input("enter marks of student4: "))

marks5 = int(input("enter marks of student5: "))

marks6 = int(input("enter marks of student6: "))

markslist = [marks1,marks2,marks3,marks4,marks5,marks6]
 
markslist.sort()
 
print(markslist) 