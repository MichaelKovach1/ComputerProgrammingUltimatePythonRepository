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
    if ValidScoreCounter == 0:
        return None
    else:
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
    if "a" in list or "e" in list or "i" in list or "o" in list or "u" in list:
         return True
    else:
         return False
print("---has_vowel---")
print(has_vowel(["a", "e", "n", "g", "h"]))
print(has_vowel(["m", "b", "n", "g", "h"]))

def all_the_same(list1):
    prev_num = list1[-1]
    truecount = 0
    for num in list1:
        if num == prev_num:
            truecount = truecount + 1
            prev_num = num
        else:
            return False
    if truecount == len(list1):
        return True
print("---all_the_same---")
print(all_the_same([1, 1]))
print(all_the_same([1, 2, 1, 1]))

def increasing(list1):
    prevnum = list1[-1]
    truecount = 0
    for num in list1:
        if num == prevnum:
            return False
        elif num == list1[0]:
            if prevnum > num:
                truecount = truecount + 1
                prevnum = num
        else:
            if num > prevnum:
                truecount = truecount + 1
                prevnum = num
            else:
                return False
    if truecount == len(list1):
        return True
print("---increasing---")
print(increasing([1, 2, 3, 5]))
print(increasing([1, 2, 2, 1, 2]))

def is_incrementing(list1):
    prevnum = list1[-1]
    truecount = 0
    for num in list1:
        if num == prevnum:
            return False
        elif num == list1[0]:
            if prevnum - num == len(list1) - 1:
                truecount = truecount + 1
                prevnum = num
        else:
            if num - prevnum == 1:
                truecount = truecount + 1
                prevnum = num
            else:
                return False
    if truecount == len(list1):
        return True
print("---is_incrementing---")
print(is_incrementing([1, 2, 3, 4, 6]))
print(is_incrementing([2, 3, 4, 5]))

def has_adjacent_repeat(list):
    prev_num = list[-1]
    complete = False
    for num in list:
        if prev_num == num:
            complete = True
        else:
            prev_num = num
    if complete == False:
        return False
    elif complete == True:
        return True
print("---has_adjacent_repeat---")
print(has_adjacent_repeat([1, 9, 2, 2, 4, 5]))
print(has_adjacent_repeat([1, 3]))

def sum_with_skips(list):
    skip_num = -1
    total = 0
    ignore = False
    seen_skip_num = False
    for num in list:
        if num == skip_num and seen_skip_num == False:
            ignore = True
            seen_skip_num = True
        elif num == skip_num and seen_skip_num == True:
            ignore = False
            seen_skip_num = False
        elif ignore == False:
            total = total + num
    return total
print("---sum_with_skips---")
print(sum_with_skips([1, 2, 3, 4, -1, 5, 6, -1, 2]))
print(sum_with_skips([4, -1, 5, -1]))
        
        
    

