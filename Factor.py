#Author: Shahnawaz Khan
#Date: 09/04/2021
#Description: Program to compute factorization of a Number entered by user
number = int (input("enter the number:"))
value = 1
print("Factor of the number {0} are:".format(number))
while (value <= number):
    if (number % value == 0):
        print("{0}".format(value))
    value = value + 1