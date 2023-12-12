import csv

f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def vowel_count(wordlist):
    most_vowels = ""
    most_vowels_count = 0
    vowel_counter = 0
    for word in wordlist:
        vowel_counter = 0
        wording = list(word)
        for letter in wording:
            if letter in "aeiou":
                vowel_counter = vowel_counter + 1
        if vowel_counter > most_vowels_count:
            most_vowels = word
            most_vowels_count = vowel_counter
    return most_vowels
print(vowel_count(words))

def average_word_length(wordlist):
    total_length = 0
    for word in wordlist:
        wording = list(word)
        for letter in wording:
            total_length = total_length + 1
    return total_length/len(wordlist)
print(average_word_length(words))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

A_count = 0
B_count = 0
C_count = 0
D_count = 0
F_count = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    if percent <= 60:
        F_count = F_count + 1
    elif percent <= 70:
        D_count = D_count + 1
    elif percent <= 80:
        C_count = C_count + 1
    elif percent <= 90:
        B_count = B_count + 1
    elif percent <= 100:
        A_count = A_count + 1
print(A_count, B_count, C_count, D_count, F_count)

f.close()

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

total_f = 0
f_count = 0
total_s = 0
s_count = 0
total_j = 0
j_count = 0
total_sr = 0
sr_count = 0
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel == 9:
        total_f = total_f + percent
        f_count = f_count + 1
    elif gradelevel == 10:
        total_s = total_s + percent
        s_count = s_count + 1
    elif gradelevel == 11:
        total_j = total_j + percent
        j_count = j_count + 1
    elif gradelevel == 12:
        total_sr = total_sr + percent
        sr_count = sr_count + 1
avgf = total_f/f_count
avgs = total_s/s_count
avgj = total_j/j_count
avgsr = total_sr/sr_count
print(avgf, avgs, avgj, avgsr)

f.close()

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
namelist = []
for row in reader:
    name, gradelevel, percent = row
    percent = int(percent)
    gradelevel = int(gradelevel)
    if gradelevel == 12 and percent <= 60:
        namelist.append(name)
print(namelist)