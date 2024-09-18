# -*- coding: utf-8 -*-
    
"""
Coders: Connor Boger, Noelle Gallagher, Quinn Geiger, Zach Johnson

Variables:
- income --> User's income for the year
- partner_income --> Partner's income for the year
- mfj --> Determines whether or not the User is married
- mfj_income --> The total houeshold income between User and Spouse
- state_tax --> The total state tax the User(s) will pay

Inputs
--> Will ask the User their income
---> Will ask the income of the User's Spouse

Outputs
"""

# User Income 

user_income = float(input("What is your income for this year? "))
 
# Is the User Single or Married?
   
mfj = input("Are you married filing jointly? - Yes or No: ")
if mfj == "Yes":
   partner_income = float(input("What is your partner's income for the year? "))
if mfj == "No":
    single_income = user_income
    

mfj_income = user_income + partner_income
if mfj == "Yes":
    print("Your household income is $", mfj_income,"!")
else:
    print("Your household income is $", single_income, "!")

#State Tax

if mfj_income <= 12420:
   state_tax = print("You owe", (mfj_income * .044), "in state taxes!")
elif mfj_income >= 12421 and mfj_income <= 62100:
    state_tax = print("You owe", 546.48 + ((mfj_income-12420)*.0482), "in state taxes!")
else:
    state_tax = print("You owe", 2941.06 + ((mfj_income-62100)*.057), "in state taxes!")

#Federal Tax

if mfj == "Yes":
    income = income - standard_deduction
