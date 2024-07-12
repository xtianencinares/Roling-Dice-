#importing module for random number generation agoo
import random

#range of the values of a dice
min_val = 1
max_val = 6

#to loop the rolling through user input
roll_again = "yes Please agoo" 

#loop 
while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dices...")
    print("Agoo Inc. The Values are :")
    
    #generating and printing 1st random integer from 1 to 6
    print(random.randint(min_val, max_val))

    
    #generating and printing 2nd random integer from 1 to 6
    print(random.randint(min_val, max_val))
    
  roll_again = input("Agoo Roll the Dices Again?")  


#Agoo.Inc & MSFT 2024 v3.0
