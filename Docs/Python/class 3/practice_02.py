#  write a program to fill a letter tamplate given below with name and date 
#  latter = dear <name>
            #  you are selected|
            #  <date>


name = input("enter your name:")
date = input("enter the date:")

template = '''
dear <|name|>
congratulations,
you are selected
<|date|>
'''
print(template.replace('<|name|>',name).replace('<|date|>',date))