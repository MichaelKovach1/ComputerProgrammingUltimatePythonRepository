import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

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
print("The Word With the Most Vowels is:", vowel_count(words))

def average_word_length(wordlist):
    total_length = 0
    for word in wordlist:
        wording = list(word)
        for letter in wording:
            total_length = total_length + 1
    return total_length/len(wordlist)
print("The Average Word Length is:", average_word_length(words))