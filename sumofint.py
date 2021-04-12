#Author: Shahnawaz Khan
#Date: 10/04/2021
#Description: A program with cubic running time. 
# Read in N integers and counts the   number of triples that sum to exactly 0


def sumofint(arr, n):
 
    found = False
    for i in range(0, n-2):
     
        for j in range(i+1, n-1):
         
            for k in range(j+1, n):
             
                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True
     
             
    
    if (found == False):
        print(" not exist ")
 

arr = [0, -4, 3, -4, 1]
n = len(arr)
sumofint(arr, n)