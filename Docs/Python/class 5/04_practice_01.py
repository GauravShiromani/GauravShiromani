# writew a program to creat a dictionaryof hindi words with value as their english
# translation provided user with an option and took it up 

oxford =  {
           "lakdi":"wood",
           "kursi":"chair",
           "roti":"bread",
           "kalam":"pen"  } 

key = input("enter the key:\n")      
if(oxford.get(key)== None):
    print("the value is not found")
else :    
 print("the value of corrensponding to your key is" ,oxford.get(key))