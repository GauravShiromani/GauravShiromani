# a spam comment is defined as a text containing a following keyword:
# "malke a lot of money" , ,"suscribe this","click this", write a program to detect this spam 

spamWords = ['buy now', 'subscribe this', 'click this']

email = input("Enter your email: ").lower()

spam = False

if('buy now' in email):
    spam = True

if('subscribe this' in email):
    spam = True

if('click this' in email):
    spam = True

print("Spam is", spam)
