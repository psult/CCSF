"""
11.15 Programming Lab 7 
Introduction To Programming With Objects

[ studentObjects.py ]

( Paulo Sultanum )
Write a program that the college Admissions office can use to manage the records of students.

"""


""" [ 1 ] 

Design and Create a Student object specification with these seven data members: name, address, city, 
state, zip, student id, and gpa."""


#creating an object class named Student, and specifying the seven data members above-mentioned.

#creating a class object representing a student, and giving it the name Student.
class Student:
    
    #creating variables with designated names and assigning to each variable an empty string as placeholder.
    name = "" 
    address = ""
    city = "" 
    state = "" 
    zip = "" 
    student_id = "" 
    
    #creating a variable for gpa, and assigning to it the float 0.00 as placeholder. 
    gpa = 0.00 



""" [ 2 ]

Within the object specification write an __init__ method to create a Student object."""


#initiating an object class named Student, using the __init__() function.

#creating a class object representing a student, and giving it the name Student.
class Student: 

    #initializing a student object witht the provided details. 
    def __init__(self, name, address, city, state, zip_code, student_id, gpa):
        
        #assigning designated self.objects to namesake variables.
        self.name = name 
        self.address = address 
        self.city = city 
        self.state = state 
        self.zip_code = zip_code 
        self.student_id = student_id 
        self.gpa = gpa 



""" [ 3 ]

Within the object specification write a method to take input for the Student object.  This method should 
be named getInput.  getInput should be programmed to use console prompts and input statements to allow the 
user to type in values for the Student object's name, address, city, state, zip, student id, and gpa data 
members.  getInput should also assign the values to each of their corresponding data members.""" 

    #defining the method getInput() 
    def getInput(self):
        
        #asking for user input, and assigning that object to an instance of the class' variable.
        self.name = input("Please type in your name: " ) 
        self.city = input("Please type in your city: " )  
        self.state = input("Please type in your state: " )  
        self.zip = input("Please type in your zip: " )  
        self.student_id = input("Please type in your student ID: " )  
        self.gpa = input("Please type in your GPA: " ) 


""" [ 4 ]

Within the object specification write a method to print output nicely formatted labels and values for a 
single student object’s data fields.  This method should be named printOutput."""


    #defining the function printOutput()
    def printOutput(self):
        
        #printing designated data member's name + "colon", a space + the data or value 
        #contained in the namesake designated variable. 
        print("name: ", name)
        print("address: ", address)
        print("city: ", city)
        print("state: ", state)  
        print("zip: ", zip)
        print("gpa: ", gpa)

""" [ 5 ]

In the main program, declare 3 uninitialized Student objects.  You may make either 3 individual objects 
make a list of 3 Student objects  -- your choice.""" 


# Creating three uninitialized Student objects.
    
Student1 = Student()
Student2 = Student()
Student3 = Student()


    

