#Author: Shahnawaz Khan
#Date: 09/04/2021
#Description: Program to prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N

Num = int(input('Enter a number'))
if Num<=0:
    print("Please enter number greater than 0")
else:
    Harmonic=0
    for i in range(1,Num+1):
        C=1/i
        Harmonic+=C
    print(Harmonic)