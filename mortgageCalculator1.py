"""
9.13 Programming Lab 6 

[ mortgageCalculator1.py ]
[ Program 1 ] 

( Paulo Sultanum )

A Simple Mortgage Calculator, v.1.0
Write a program to determine the monthly payment on borrowed amount of money to be paid back over 30 years.
"""

""" [ 1 ] 

Choose a dollar amount to be borrowed, as a whole number. 
"""

#ask user to input the amount borrowed and assign the input to the variable p.
p = float(input("Please type the amount borrowed ", ))#assigned as floating point since int throws an error.


""" [ 2 ] 

Specify an annual percent interest rate, as a floating-point number.
"""

#ask user to input the interest rate and assign the input as a foating point to the variable r.
r = float(input("Please type the interest rate ", ))

#ask user to input the payback period and assign the input as a floating point to the variable n.
n = float(input("Please type the payback period in months ", ))#assigned as floating point since int throws 
                                                                #an error.

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

#printing the outputs from variables p, r and n.
print("Amount Borrowed: ,", p)
print("Annual Interest Rate: ", r)
print("Payback Periode: ", n)
print(" ")


""" [ 5 ] 

Include in the output the calculated monthly payment, formatted to show two decimal places
(like this: 1000.00). 
"""
#format monthly payment to show two decimal points.
fmp = f"{mp:.2f}"

# print monthly payment and the formatted result. 
print("Monthly payment: ", fmp)
