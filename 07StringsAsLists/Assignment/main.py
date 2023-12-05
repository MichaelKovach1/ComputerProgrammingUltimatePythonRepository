def is_alliteration(word1, word2):
    firstletter1 = word1[0]
    firstletter2 = word2[0]
    if firstletter1 == firstletter2:
        return True
    else:
        return False
print("---is_alliteration---")
print(is_alliteration("Jumper", "Jelly"))
print(is_alliteration("Walk", "Drive"))

def count_vowels(word):
    vowel_counter = 0
    for letter in word:
        if letter in "aeiou":
            vowel_counter = vowel_counter + 1
        else:
            vowel_counter = vowel_counter
    return vowel_counter
print("---count_vowels---")
print(count_vowels("Hello"))
print(count_vowels("Drinkable"))

def count_numbers(string):
    number_counter = 0
    for character in string:
        if character in "1234567890":
            number_counter = number_counter + 1
        else: number_counter = number_counter
    return number_counter
print("---count_numbers---")
print(count_numbers("A1229jk"))
print(count_numbers("Llk4j3ils"))

def count_target_letters(word, letter):
    target_letter = letter
    target_letter_counter = 0
    for letters in word:
        if letters == target_letter:
            target_letter_counter = target_letter_counter + 1
        else:
            target_letter_counter = target_letter_counter
    return target_letter_counter
print("---count_target_letters---")
print(count_target_letters("Barracuda", "a"))
print(count_target_letters("Grappling", "p"))

def in_alphabetical_order(word):
    winner = "0"
    true_count = 0
    for letter in word:
        if letter > winner:
            winner = letter
            true_count = true_count + 1
        else:
            winner = winner
    if true_count == len(word):
        return True
    else: 
        return False
print("---in_alpabetical_order---")
print(in_alphabetical_order("brink"))
print(in_alphabetical_order("is"))
