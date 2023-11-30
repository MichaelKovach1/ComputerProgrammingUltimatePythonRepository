def count_failing_grades(GradeList):
    gradecount = int(0)
    for grade in GradeList:
        if grade < 60:
           gradecount = gradecount + 1
        else:
            gradecount = gradecount
    return gradecount
inputlist = [100, 95, 78, 40, 50]
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
print(count_act_scores(inputList))

def number_sum(NumberList):
    Total = 0
    for number in NumberList:
        Total = Total + number
    return Total
InputList = [1, -2, 3, 4, 20]
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
print(average_act_score(Inputlist))