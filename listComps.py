"""
8.9 Programming Lab 5 

[ listCompss.py ]
[ Program 3 ] 

( Paulo Sultanum )

Write a program named listComps.py that has the following:
"""


""" [ 1 ] 

These lists:
"""
#declaring the variables A and B with the provided list of elements.
A = [1,2,3,4,5]
B = [2,4,6,8,10]


""" [ 2 ] 

One list comprehension that makes a list which multiplies all of the elements of A by 7.  
Store this list in a variable called S.  Once S is made, print S.
"""

#declare variable S, and create a list comprehension which multiplies all of the elements of A by 7,
#and stores the new list in the variable S.
S = [ i*7 for i in A]

#printing "S is" + the result contained in the variable S.
print("S is", S)

""" [ 3 ] 

A second list comprehension that takes all of the elements of both list A and list B selects only those 
elements that are even.  Store this list in a variable called Even.  Once Even is made, print Even.
"""

#declare the variable Even, and create a list comprehension that takes all of the elements of both list 
#A and list B, selects only those elements that are even and stores the new list in the variable Even.
Even = [ i for i in A and B if i%2 == 0 ]

#printing "Even is" + the result contained in the variable Even.
print("Even is", Even)


""" [ 4 ]

A third list comprehension that multiples all of the elements of A with all of the elements of B.  
Store this list in a variable called multiples.  Once multiples is made, print multiples.  
"""

#declare the variable multiples, and create a list comprehension that multiples all of the elements of A, 
#with all of the elements of B, and stores the new list in the variable multiples.
multiples = [ i*j for i in A for j in B ]

#printing "multiples is" + the result contained in the variable multiples.
print("multiples is", multiples)

