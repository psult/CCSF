"""
Programming Exercise 9:  Regular Expressions

[ regexpsWith4Strings.py ]

( Paulo Sultanum )

-Use the Python re module and regular expression match objects
-Create 3 regular expressions that will be used to check for patterns in 4 separate strings

In this lab you will have 4 strings that will be searched to see if they match some regular expressions.  

The 4 strings you are to use are: 
string1 = "A man a plan a canal panama".
string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
string3 = "alphabravocharliedeltaechofoxtrot"
string4 = "0123456789"

Each of the 4 strings mentioned above should be tested using regular expressions.  
Each string should use a re object to see if it matches

(1) a regular expression that matches something that has one or more lowercase letters
(2) a regular expression that matches something that has one or more uppercase letters
(3) a regular expression that matches something that has one or more digits 
                                        (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9)."""

# Import re module.
import re

""" [ 1 ] 

string1 = "A man a plan a canal panama"."""

"""(1) a regular expression that matches something that has one or more lowercase letters
import re"""

 # Define the sentence to apply regex.
sentence = "A man a plan a canal panama"

# Define the regex.
pattern = r'[a-z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check for a match.
if match:
    print("string1 matches a regular expression which indicates it has lowercase letters.")
else:
    print("string1 does not match a regular expression which indicates it does not have lowercase letters.")


"""(2) a regular expression that matches something that has one or more uppercase letters"""

 # Define the sentence to apply regex.
sentence = "A man a plan a canal panama"

# Define the regex.
pattern = r'[A-Z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check if there's a match
if match:
    print("string1 matches a regular expression which indicates it has uppercase letters.")
else:
    print("string1 does not match a regular expression which indicates it does not have uppercase letters.")
    

"""(3) a regular expression that matches something that has one or more digits 
                                        (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9)."""
  
 # Define the sentence to apply regex.
sentence = "A man a plan a canal panama"

# Define the regex.
pattern = r'\d+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check for a match.
if match:
    print("string1 does match a regular expression which indicates it has digits.")
else:
    print("string1 does not match a regular expression which indicates it does not have digits.")
    
    
""" [ 2 ] 

string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"."""
    
"""(1) a regular expression that matches something that has one or more lowercase letters
import re"""
 
 # Define the sentence to apply regex.
sentence = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
 
 # Define the regex.
pattern = r'[a-z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

 # Check for a match.
if match:
     print("string2 matches a regular expression which indicates it has lowercase letters.")
else:
    print("string2 does not match a regular expression which indicates it does not have lowercase letters.")
    
"""(2) a regular expression that matches something that has one or more uppercase letters"""
    
 # Define the sentence to apply regex.
sentence = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"

# Define the regex.
pattern = r'[A-Z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check if there's a match
if match:
    print("string2 matches a regular expression which indicates it has uppercase letters.")
else:
    print("string2 does not match a regular expression which indicates it does not have uppercase letters.")
    
"""(3) a regular expression that matches something that has one or more digits 
                                        (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9)."""
  
 # Define the sentence to apply regex.
sentence = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"

# Define the regex.
pattern = r'\d+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check for a match.
if match:
    print("string2 does match a regular expression which indicates it has digits.")
else:
    print("string2 does not match a regular expression which indicates it does not have digits.")
    
    
""" [ 3 ] 

string3 = "alphabravocharliedeltaechofoxtrot"."""

    
"""(1) a regular expression that matches something that has one or more lowercase letters
import re"""
 
 # Define the sentence to apply regex.
sentence = "alphabravocharliedeltaechofoxtrot"
 
 # Define the regex.
pattern = r'[a-z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

 # Check for a match.
if match:
     print("string3 matches a regular expression which indicates it has lowercase letters.")
else:
    print("string3 does not match a regular expression which indicates it does not have lowercase letters.")
 
   
"""(2) a regular expression that matches something that has one or more uppercase letters"""
    
 # Define the sentence to apply regex.
sentence = "alphabravocharliedeltaechofoxtrot"

# Define the regex.
pattern = r'[A-Z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check if there's a match
if match:
    print("string3 matches a regular expression which indicates it has uppercase letters.")
else:
    print("string3 does not match a regular expression which indicates it does not have uppercase letters.")
 
  
"""(3) a regular expression that matches something that has one or more digits 
                                        (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9)."""
  
 # Define the sentence to apply regex.
sentence = "alphabravocharliedeltaechofoxtrot"

# Define the regex.
pattern = r'\d+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check for a match.
if match:
    print("string3 does match a regular expression which indicates it has digits.")
else:
    print("string3 does not match a regular expression which indicates it does not have digits.")
    

""" [ 4 ] 

string4 = string4 = "0123456789"."""

"""(1) a regular expression that matches something that has one or more lowercase letters
import re"""
 
 # Define the sentence to apply regex.
sentence = "0123456789"
 
 # Define the regex.
pattern = r'[a-z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

 # Check for a match.
if match:
     print("string4 matches a regular expression which indicates it has lowercase letters.")
else:
    print("string4 does not match a regular expression which indicates it does not have lowercase letters.")
 
   
"""(2) a regular expression that matches something that has one or more uppercase letters"""
    
 # Define the sentence to apply regex.
sentence = "0123456789"

# Define the regex.
pattern = r'[A-Z]+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check if there's a match
if match:
    print("string4 matches a regular expression which indicates it has uppercase letters.")
else:
    print("string4 does not match a regular expression which indicates it does not have uppercase letters.")
 
  
"""(3) a regular expression that matches something that has one or more digits 
                                        (that is, 0, 1, 2, 3, 4, 5, 6, 7, 8, or 9)."""
  
 # Define the sentence to apply regex.
sentence = "0123456789"

# Define the regex.
pattern = r'\d+'

# Use re.search() to look for the pattern.
match = re.search(pattern, sentence)

# Check for a match.
if match:
    print("string4 does match a regular expression which indicates it has digits.")
else:
    print("string4 does not match a regular expression which indicates it does not have digits.")
string4 = "0123456789"
    