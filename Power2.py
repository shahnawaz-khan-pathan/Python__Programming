#Author: Shahnawaz Khan
#Date: 09/04/2021
#Description: This program takes a command-line argument N 
#and prints a table of the powers of 2

num = int(input("enter a number:"))

print("multiplication table of", num)
for i in range(1, 11):
     print(num,"x",i,"=",num * i)