#Author: Shahnawaz Khna
#Date: 09/04/2021
#Description: A library for reading in 2D arrays of integers, doubles, or booleans 
# from standard input and printing them out to standard output


def PrintArray(R,C):
   
    array = []
    print("Enter the element:")
  
    
    for i in range(R):          
        a =[]
        for j in range(C):     
            a.append(input())
        array.append(a)
     
  
    for i in range(R):
        for j in range(C):
            print(array[i][j], end = " ")
        print()
         
try:
    PrintArray(4,4)
except Exception as e:
    print("invalid input",e)
