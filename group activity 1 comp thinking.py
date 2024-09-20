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

user_income = float(input("What is your income for the year? "))
standard_deduction1 = 14600
standard_deduction2 = 29200
# Check filing status

mfj = input("Are you married filing jointly? - Yes or No: ")
if mfj == "Yes":
   partner_income = float(input("What is your partner's income for the year? "))
   mfj_income = user_income + partner_income
   print("Your household income is $", mfj_income,"!")   
else:
   single_income = user_income 
   print("Your household income is $", single_income, "!")
    
#State Tax

if mfj == "Yes":
   if mfj_income <=12420:
       state_tax = print("You owe", (mfj_income * .044), "in state taxes in 2024!")
   elif mfj_income >= 12421 and mfj_income <= 62100:
       state_tax = print("You owe", 546.48 + ((mfj_income-12420)*.0482), "in state taxes in 2024!")
   elif mfj_income > 62100:
       state_tax = print("You owe", 2941.06 + ((mfj_income-62100)*.057), "in state taxes in 2024!")
    
if mfj == "No":    
    if single_income >= 0 and single_income <= 6210:
        state_tax = print("You owe", (single_income *.044), "in state taxes in 2024!")
    elif single_income > 6210 and single_income <=31050:
        state_tax = print("You owe", (273+(single_income - 6210) * .0482), "in state taxes in 2024!") 
    elif single_income >31050:
        state_tax = print("You owe", (1470.53+(single_income - 31050) * .057), "in state taxes in 2024!")
#Federal Tax

   
if mfj == "Yes":
    taxable_mfj = mfj_income - standard_deduction2
    if taxable_mfj <= 23200 :
        federal_tax = print("You owe", (taxable_mfj * .10), "in federal taxes!")
    elif taxable_mfj >= 23201 and taxable_mfj <= 94300 :
        federal_tax = print("you owe", 2320 + ((taxable_mfj - 23200 )* .12),"in federal taxes in 2024!")
    elif taxable_mfj >=94301 and taxable_mfj <201050 :
        federal_tax = print("you owe" ,10852 + ((taxable_mfj - 94300) * .22), "in federal taxes in 2024!")
    elif taxable_mfj >= 201051 and taxable_mfj <= 383900 :
        federal_tax = print("You owe" ,34337 + ((taxable_mfj - 201050) * .24), "in federal taxes in 2024!")
    elif taxable_mfj >= 383901 and taxable_mfj <= 487450 :
        federal_tax = print("You owe" ,78221 + ((taxable_mfj - 383900) * .32), "in federal taxes in 2024!")
    elif taxable_mfj >= 487451 and taxable_mfj <= 731200:
        federal_tax = print("You owe" ,111357 + ((taxable_mfj - 487450) * .35), "in federal taxes in 2024!")
    elif taxable_mfj >= 731201:
        federal_tax = print("You owe", 196669.50 + ((taxable_mfj - 731200) * .37), "in federal taxes in 2024!")
        
if mfj == "No" :
    taxable_s = single_income - standard_deduction1    
    if taxable_s <= 11600:
        federal_tax = print("You owe", (taxable_s * .1)),"in federal taxes in 2024!"
    elif taxable_s >=11600 and taxable_s <=47150 :
        federal_tax = print("You owe", 1160 + (taxable_s - 11600)*.12, "in federal taxes in 2024!" )
    elif taxable_s >= 47151 and taxable_s <=100525:
        federal_s = print("You owe", 5426 + (taxable_s - 47150)*.22, "in federal taxes in 2024!")
    elif taxable_s >=100526 and taxable_s <=191950 :
        federal_tax = print("You owe", 17168.5 + (taxable_s - 100525)*.24, "in federal taxes in 2024!")
    elif taxable_s >=19151 and taxable_s <= 243725:
        federal_s = print("You owe", 39110.5 + (taxable_s - 191950)*.32, "in federal taxes in 2024!")
    elif taxable_s >= 243726 and taxable_s <= 609350:
        federal_s = print("You owe", 55678.5 + (taxable_s - 243725)*.35, "in federal taxes in 2024!" )
    elif taxable_s > 609351:
        federal_s = print("You owe", 183647.25 + (taxable_s - 609350)*.37, "in federal taxes in 2024!")


if mfj == "Yes":
    print("Your total taxes for 2024 are", (state_tax + federal_tax))

if mfj == "No":
    print("Your total taxes for 2024 are", (state_tax + federal_s))




    


