# write a program to find greatest of four numbers entered by the user 

a = 42
b = 243
c = 9
d = 13

if a > b :

    maxNum1 = a
else :
    maxNum1 = b

if c > d :
    maxNum2 = c
else :
    maxNum2 = d

if (maxNum2 > maxNum1):
    maxNum = maxNum2
else :  maxNum = maxNum1

print("the maximum no of out of these is" , maxNum)