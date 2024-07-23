"""
14.14 Programming Lab 10

[ openStudentFiledException1.py ]

( Paulo Sultanum )

"""
# Import re module.
import re

""" [ Program 2 ] 

Write a program named openStudentFileException1.py.  openStudentFileException1.py also attempts to open a 
file named student.txt.  Once again, this student.txt file may or may not exist at the time you first 
run your program.  

Requirements.
openStudentFiledException1.py needs to have inside its main program the following programming logic:
try:
    with open the student.txt file for reading as give a file_handler:
        # place programming logic underneath the with statement that
        # prints a message saying "The student.txt file was found."
except a Python exception that is appropriate for not being able to open a file:          
    # place programming logic underneath the except statement to print an
    # error message that says "Sorry, the student.txt file was not found."
    # if the student.txt file is not available.
"""

def main():
    try:
        # Attempts to open and read the student.txt file.
        with open('student.txt', 'r') as file_handler:
            # Prints a message if the file is found and opened successfully.
            print("The student.txt file was found.")
    except FileNotFoundError:
        # Prints an error message if the student.txt file is not found.
        print("Sorry, the student.txt file was not found.")

if __name__ == "__main__":
    main()
