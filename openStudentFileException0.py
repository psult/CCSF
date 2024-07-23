"""
14.14 Programming Lab 10

[ openStudentFiledException0.py ]

( Paulo Sultanum )

"""
# Import re module.
import re

""" [ Program 1 ] 

Write a program named openStudentFileException0.py. openStudentFileException0.py attempts to open a 
file named student.txt.  This student.txt file may or may not exist at the time you first run your program.  

Requirements.
openStudentFiledException0.py needs to have inside its main program the following programming logic:
try:
     # place programming logic underneath the try statement to open the student.txt file.  
     # the programming logic must use the open function to attempt to open student.txt for reading.
except:
     # place programming logic underneath the except statement to print an
     # error message that says "Sorry, the student.txt file was not found."
     # if the student.txt file is not available.
"""

def main():
    try:
        # Attempts to open and read the student.txt file.
        with open('student.txt', 'r') as file:
            # Prints a message if the file is found and opened successfully.
            print("The student.txt file was found.")
    except FileNotFoundError:
        # Prints an error message if the student.txt file is not found.
        print("Sorry, the student.txt file was not found.")

if __name__ == "__main__":
    main()
