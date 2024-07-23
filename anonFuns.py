"""
8.9 Programming Lab 5 

[ anonFuns.py ]
[ Program 2 ] 

( Paulo Sultanum )

Write a program named anonFuns.py that has the following:
"""


""" [ 1 ] 

A list of values from 1 to 10 in your program:  
"""
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


""" [ 2 ] 

One anonymous function that you create which finds the maximum value of two parameters passed to it.

In other words, the anonymous function you are creating takes two parameters, and returns whichever of 
the two parameters has the larger value. Using this anonymous function that you create, find the maximum 
value in myList.  Assign the maximum value to the variable maxMyList, and print maxMyList out after it 
has been assigned.  
"""
#anonymous function that you create which finds the maximum value of two parameters passed to it
maxMyList = lambda x, y: x if x > y else y

#use reduce() function to find the max value in myLIst
from functools import reduce

#assign the maximum value to the variable maxMyList 
max_value = reduce(maxMyList, myList)

#print maxMyList
print(max_value) 

""" [ 3 ] 

A second anonymous function that you create which takes a single parameter and returns that parameter 
squared.  In other words, the lambda function returns the single parameter multiplied by itself.  

You must use map() to call the lambda function on myList, and return values that the lambda function 
you create has used with map() to make the square of each element in myList. 

Once you place your lambda function in map(), store what map() makes into a list variable named 
return_results.  This means return_results is supposed to be a list of the results of the myList values 
multiplied by themselves. 

Remember, map() returns list items without actually making a list (the technical name for all these items 
is an iterable).  So you will have to use what map() returns and the function list() since the function 
list() takes list items that are given to it, and then makes a list with the items given to it. 

This means that you will need to use both map() and list() together to make return_results a list. 
Once return_results is a list, print return_results.
"""
squareF = lambda m : m**m
return_results = map(squareF, (myList))
print(list(return_results))
