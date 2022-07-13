
# a = [1,2,3,4,5,6]

# for item in a:
   
#     print(item)
    
#     if (item==4):
#          break
# print("we have finished this loop")

a = [1,2,3,4,5,6]

for item in a:
   print(item)
   if(item== 4):
    continue
   print("done this iteration for" ,item)
print("we have finished this loop")