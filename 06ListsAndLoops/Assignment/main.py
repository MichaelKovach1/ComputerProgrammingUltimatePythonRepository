def count_failing_grades(GradeList):
    gradecount = int(0)
    for grade in GradeList:
        if grade < 60:
           gradecount = gradecount + 1
        else:
            gradecount = gradecount
    return gradecount
inputlist = [100, 95, 78, 40, 50]
print("---count_failing_grades---")
print(count_failing_grades(inputlist))

def count_act_scores(scoreList):
    counter = int(0)
    for score in scoreList:
        if score >= 1 and score <= 36:
            counter = counter + 1
        else:
            counter = counter
    return counter
inputList = [36, 45, 20, 1, 19]
print("---count_act_scores---")
print(count_act_scores(inputList))

def number_sum(NumberList):
    Total = 0
    for number in NumberList:
        Total = Total + number
    return Total
InputList = [1, -2, 3, 4, 20]
print("---number_sum---")
print(number_sum(InputList))

def average_act_score(scoreList):
    Total = 0
    ValidScoreCounter = 0
    for score in scoreList:
        if score >= 1 and score <= 36:
            Total = Total + score
            ValidScoreCounter = ValidScoreCounter + 1
        else:
            ValidScoreCounter = ValidScoreCounter
            Total = Total
    mean = Total/ValidScoreCounter
    return mean
Inputlist = [36, 45, 28, 13, 19]
print("---average_act_score---")
print(average_act_score(Inputlist))

def all_true(list1):
    true_counter = 0
    for boolean in list1:
        if boolean == True:
            true_counter = true_counter + 1
        else:
            true_counter = true_counter
    if true_counter == len(list1):
        return True
    else:
        return False
list1 = [True, True, True, True, True]
list2 = [True, True, True, True, False]
print("---all_true---")
print(all_true(list1))
print(all_true(list2))

def any_true(list):
    if True in list:
         return True
    else:
         return False
print("---any_true---")
print(any_true([True, False, False]))
print(any_true([False, False, False]))

def mostly_true(list):
    true_counter = 0
    false_counter = 0
    for boolean in list:
        if boolean == True:
            true_counter = true_counter + 1
        elif boolean == False:
            false_counter = false_counter + 1
    if true_counter > false_counter:
        return True
    elif false_counter >= true_counter:
        return False
print("---mostly_true---")
print(mostly_true([True, False, True, False]))
print(mostly_true([True, True, True, False]))

def has_vowel(list):
    if "a" in list or "e" in list or "i" in list or "o" in list or "u" in list or "y" in list:
         return True
    else:
         return False
print("---has_vowel---")
print(has_vowel(["a", "e", "n", "g", "h"]))d
print(has_vowel(["m", "b", "n", "g", "h"]))
    

