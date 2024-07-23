""" 
8.9 Programming Lab 5 

[ coinToss.py ]
[ Program 1 ] 

( Paulo Sultanum )

Write a computer game program, from scratch, using if-logic and count-controlled loops which 
requires using a Python Built-in module.
Write a program named coinToss.py that allow the user to specify by using keyboard input the number of coin 
tosses to perform when you run the program, and have the program display the result of each coin toss.
"""

#import random library
import random 

#Have the user to enter how many coin tosses to perform
print("Please type how many coin tosses you would like to perform")

#Input and store the user's value for how many coin tosses to perform
_input = input()

#Create a counter variable and set it to zero
counter = 0

#Start the loop here    
if counter == _input:
    Break 
    
#Get and store a randomly-generated number in the range 0 to 1
ran = random.randint(0, 1)

#If the randomly-generated number equals 0 Output "heads"         
if ran == 0:
    print("Heads")
    
#If the randomly-generated number equals 1 Output "tails"        
if ran == 1:
    print("Tails")
    
#Add one to the counter variable
    counter += 1

