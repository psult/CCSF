"""
9.13 Programming Lab 6 

[ mortgageCalculator2.py ]
[ Program 2 ] 

( Paulo Sultanum )

Modify your mortgageCalculator1.py program to do the following:
"""

"""
ORIGINAL CODE
"""

""" [ 1 ] 

Choose a dollar amount to be borrowed, as a whole number. 
"""

#ask user to input the amount borrowed and assign the inut to the variable p.
p = int(input("Please type the amount borrowed ", ))


""" [ 2 ] 

Specify an annual percent interest rate, as a floating-point number.
"""

#ask user to input the interest rate and assign the inut to the variable r.
r = float(input("Please type the interest rate ", ))

#ask user to input the payback period  and assign the input to the variable n.
n = (float(input("Please type the payback period in months ", ))) 

""" [ 3 ] 

Calculate the monthly payment in dollars, as a floating-point number. 
(p * (1 + r)**n * r) / ((1 + r)**n - 1)
• p is the mortgage amount as entered by the user
• r is the monthly decimal interest rate
• n is the number of monthly payments in the payback period
"""

#calculating monthly payment and assigning the result to the variable mp.
mp = (p * (1 + r)**n * r) / ((1 + r)**n - 1) / 1000

""" [ 4 ] 

Include in the output an echo of the input amount borrowed, the annual percent interest rate
(without formatting) and the payback period (in years). 
"""

#print("Amount Borrowed: ,", p)
#print("Annual Interest Rate: ", r)
#print("Payback Periode: ", n)
#print(" ")


""" [ 5 ] 

Include in the output the calculated monthly payment, formatted to show two decimal places
(like this: 1000.00). 
"""
#format monthly payment to show two decimal points
fmp = f"{mp:.2f}"

#print("Monthly payment: ", fmp)

"""
M-O-D-I-F-I-E-D   C-O-D-E
"""

""" [ 1 ] 

Output the prompts and input for amount borrowed, the annual percent interest rate (without formatting) 
and the payback period (in years).  Make sure you write the output to the output file this time and not 
to the console screen.
"""
# Open the file in write mode ('w')
with open('mortgageOutput.txt', 'w') as f:
    # Write the variables p, r and n to the file
    f.write("Amount Borrowed: " + str(p) + "\n")
    f.write("Annual Interest Rate: " + str(r) + "\n")
    f.write("Payback Periode: "+ str(n / 12) + "\n")
    
    """ [ 2 ] 

 Include in the output the calculated monthly payment, formatted to show two decimal places 
 (like this: 1000.00) 
"""
    f.write("Monthly payment: " + str(fmp))
   




    