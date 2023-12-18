import json
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
f = open("../data/childDetails.json", "r")
children = json.load(f)
longest_name = ""
longest_name_length = 0
for child in children:
    if len(child["name"]) >= longest_name_length:
        longest_name_length = len(child["name"])
        longest_name = child["name"]
    guardians = child["guardians"]
    for guardian in guardians:
        if len(guardian["name"]) >= longest_name_length:
            longest_name_length = len(guardian["name"])
            longest_name = guardian["name"]
    siblings = child["siblings"]
    for sibling in siblings:
        if len(sibling["name"]) >= longest_name_length:
            longest_name_length = len(sibling["name"])
            longest_name = sibling["name"]
print("The Person With the Longest Name in This List is:", longest_name)

income_total = 0
max_income_total = -99999999999999999999
child_max_income_total = ""
min_income_total = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
child_min_income_total = ""
for child in children:
    guardians = child["guardians"]
    for gaurdian in guardians:
        income_total = income_total + gaurdian["salary"]
    if income_total >= max_income_total:
        max_income_total = income_total
        child_max_income_total = child["name"]
    if income_total <= min_income_total:
        min_income_total = income_total
        child_min_income_total = child["name"]
print("The Child With the Highest Household Income in This List is:", child_max_income_total)
print("The Child With the Lowest Household Income in This List is:", child_min_income_total)

income_total = 0
allowance = 0
max_allowance_total = -99999999999999999999
child_max_allowance_total = ""
min_allowance_total = 99999999999999999999999999999999999999999999999999999999999999999999999999999999
child_min_allowance_total = ""
for child in children:
    number_of_siblings = len(child["siblings"])
    guardians = child["guardians"]
    for gaurdian in guardians:
        income_total = income_total + gaurdian["salary"]
    if number_of_siblings == 0:
        allowance = income_total
    else:
        allowance = income_total/number_of_siblings
    if allowance >= max_allowance_total:
        max_allowance_total = allowance
        child_max_allowance_total = child["name"]
    if allowance <= min_allowance_total:
        min_allowance_total = allowance
        child_min_allowance_total = child["name"]
print("The Child With the Highest Inheritance in This List is:", child_max_allowance_total)
print("The Child With the Lowest Inheritance in This List is:", child_min_allowance_total)