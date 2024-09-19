# -*- coding: utf-8 -*-
    
"""
Coders: Connor Boger, Noelle Gallagher, Quinn Geiger, Zach Johnson

Variables:
- income --> User's income for the year
- partner_income --> Partner's income for the year
- mfj --> Determines whether or not the User is married
- mfj_income --> The total houeshold income between User and Spouse
- singe_income --> Portrayal of the User's income if the User is single
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

standard_deduction1 = 14600
standard_dedudction2 = 29200
if mfj == "Yes":
    taxable_mfj = mfj_income - standard_deduction2
if mfj == "No" :
    taxable_mfj = income - standard_deduction1
    
if taxable_mfj < 0 :
    federal_tax = print("You owe $0 in federal taxes!")
elif taxable_mfj <= 23200 :
    federal_tax = print("You owe", (taxable_mfj * .10) "in federal taxes!")
elif taxable_mfj >= 23201 and <= 94300 :
    federal_tax = print("you owe", 2320 + ((taxable_mfj - 23200 )* .12) "in federal taxes!")
elif taxable_mfj >=94301 and <201050 :
    federal_tax = print("you owe" 10852 + ((taxable_mfj - 94300) * .22) "in federal taxes!")
elif taxable_mfj >= 201051 and <= 383900 :
    federal_tax = print("You owe" 34337 + ((taxable_mfj - 201050) * .24) "in federal taxes!")
elif taxable_mfj >= 383901 and <= 487450 :
    federal_tax = print("You owe" 78221 + ((taxable_mfj - 383900) * .32) "in federal taxes!")
elif taxable_mfj >= 487451 and <= 731200
    print("You owe" 111357 + ((taxable_mfj - 487450) * .35) "in federal taxes!")
else taxable_mfj >= 731201
    print("You owe" 196669.50 + ((taxable_mfj - 731200) * .37) "in federal taxes")






    


