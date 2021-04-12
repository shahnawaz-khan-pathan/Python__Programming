#Author: Shahnawaz khan
#Date: 09/04/2021
#Description: Program to take username as input from user and validate it


str = "Hello <<UserName>>, How are you?"
name= input("Enter your name here ")
if len(name) < 3:
    print('min three characters')
else:
    str = str.replace("<<UserName>>",name)
    print(str)