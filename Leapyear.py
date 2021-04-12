#Author: Shahnawaz Khan
#Date: 09/04/2021
#Description: Program to Find a year entered by user is a Leap year or Not

year=int(input("Enter year to be checked:"))
if year<1000:
    print('invalid year, please enter 4 digit year value')
else:
 if(year%4==0 and year%100!=0 or year%400==0):
    print('The year is a leap year!')
 else:
    print('The year isnt a leap year!')