import random

#Author: Shahnawaz Khan
#Date: 09/04/2021
#Description: Program to Flip coin and print percentage of Heads and Tails
def flipCoin():
    heads = 0 
    tails = 0 
    headspercent = 0 
    tailspercent = 0 

    for i in range(1000): 
      coin=random.randint(1,2) 

      if coin==1: 
          heads+=1 
      else: 
          tails+=1 

    headspercent = heads / 10.0 
    tailspercent = 100.0 - headspercent 

    print("Heads percent: " + str(headspercent)) 
    print("Tails percent: " + str(tailspercent)) 



flipCoin()