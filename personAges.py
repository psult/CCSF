"""
12.11 Programming Lab 8 
Inheritance With Objects

[ personAges.py ]

( Paulo Sultanum )

Write a program named personAges.py.  Here are the specifications for personAges.py:"""


""" [ 1 ] 

Use this Human class in the program:"""

class Human:
    name = None
    age = None
    
    def __init__(self):
        self.name = None
        self.age = None

    def set_name(self,name):
        self.name = name
        
    def set_age(self,age):
        self.age = age

    def get_age(self):
        return self.age


""" [ 2 ]

Make a class named Youth.  The Youth class should inherit from the Human class.  
Define a method inside the class named age_appropriate().  age_appropriate() should use the age data 
member of a Youth object to perform the following logic:

if the get_age() method returns a value that is greater than or equal to 18:
               print("You're old for a Youth!")

else:
               print("Nice to meet you young person.")"""

class Youth(Human):
    def age_appropriate(self):
        if self.get_age() >= 18:
            print("You're old for a Youth!")
        else:
            print("Nice to meet you young person.")


""" [ 3 ]

Make a class named Elder.  The Elder class should inherit from the Human class.  
Define a method inside the class named age_appropriate().  This age_appropriate() method should perform 
the following logic:

if the get_age() method returns a value that is less than 70:
               print("You're young for an Elder!")

else:
              print("Nice to meet you most venerable Senior.")""" 

class Elder(Human):
    def age_appropriate(self):
        if self.get_age() < 70:
            print("You're young for an Elder!")
        else:
            print("Nice to meet you most venerable Senior.")


""" [ 4 ]

In the main program, make a single object variable called person. 

Make the person object variable an instance of the Youth class.  
After the person object is instantiated,assign the age data member to be 10 with the object's set_age() method.  
After the age is assigned to 10, have the object perform its age_appropriate() method.  
Once the object's age_appropriate method() is performed, assign the age data member to be 20.  
After the age is assigned to 20, have the object perform its age_appropriate() method."""

# make a single object variable called person. Make the person object variable an instance of the Youth 
# class. 
person = Youth()

#ask user to input the age (10).
set_age1 = int(input("Enter an age for the person: ", ))

# assign the age data member to be the user input (10) with the object's set_age() method.
person.set_age(set_age1)

# have the object perform its age_appropriate() 
person.age_appropriate()  

#ask user to input the age (20).
set_age2 = int(input("Enter an age for the person: ", ))

#  assign the age data member to be the user input (20) with the object's set_age() method.
person.set_age(set_age2)

# # have the object perform its age_appropriate()
person.age_appropriate()  


""" [ 5 ]

In the main program, you'll now demonstrate a basic form of polymorphism by doing the following --

Using the same person object variable from step 4, reassign the person object variable to be an instance 
of the Elder class.  After the person object is instantiated, assign the age data member to be 55 with the 
object's set_age() method.  After the age is assigned to 55, have the object perform its age_appropriate() 
method.  Once the object's age_appropriate method() is performed, assign the age data member to be 75.  
After the age is assigned to 75, have the object perform its age_appropriate() method..""" 


# reassign the object variable person to be an instance of the Elder class. 
person = Elder()

#ask user to input the age (55).
set_age3 = int(input("Enter an age for the person: ", ))

# assign the age data member to be the user input (55) with the object's set_age() method.
person.set_age(set_age3)

# have the object perform its age_appropriate() method.
person.age_appropriate()

#ask user to input the age (75).
set_age4 = int(input("Enter an age for the person: ", ))

# assign the age data member to be the user input (75) with the object's set_age() method.
person.set_age(set_age4)

# have the object perform its age_appropriate() method
person.age_appropriate()
