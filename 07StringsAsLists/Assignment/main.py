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

def alternate_case(word):
    result = ""
    letter_counter = 1
    uppercase = False
    for letter in word:
        if letter_counter == 1:
            uppercase = True
            letter_counter = 0
        elif letter_counter == 0:
            uppercase = False
            letter_counter = 1
        if uppercase == True:
            result = result + letter.upper()
        elif uppercase == False:
            result = result + letter.lower()
    return result
print("---alternate_case---")
print(alternate_case("hello"))
print(alternate_case("better"))

def remove_vowels(word):
    result = ""
    for letter in word:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result
print("---remove_vowels---")
print(remove_vowels("bazinga"))
print(remove_vowels("jello"))

def to_camel_case(string):
    result = ""
    nextcapital = False
    for character in string:
        if character == " ":
            nextcapital = True
        else:
            if nextcapital == True:
                result = result + character.upper()
                nextcapital = False
            elif nextcapital == False:
                result = result + character.lower()
    return result
print("---to_camel_case---")
print(to_camel_case("hi im josh"))
print(to_camel_case("how is your day"))

def to_snake_case(string):
    result = ""
    underscore = "_"
    for character in string:
        if character == " ":
            result = result + underscore
        else:
            result = result + character
    return result
print("---to_snake_case---")
print(to_snake_case("i want a small drink please"))
print(to_snake_case("go fish"))

def without_duplicates(list):
    banlist = "a"
    result = []
    for integer in list:
        if integer == banlist:
            banlist = integer
            pass
        else:
            result.append(integer)
            banlist = integer
    return result
print("---without_duplicates---")
print(without_duplicates([1, 2, 3, 4, 2, 5]))
print(without_duplicates([1, 1, 1, 1, 3, 1, 1, 3]))

def filter_valid_act_scores(list):
    result = []
    for score in list:
        if score >= 1 and score <= 36:
            result.append(score)
        else:
            pass
    return result
print("---filter_valid_act_scores---")
print(filter_valid_act_scores([1, 2, 50, 46, 19]))
print(filter_valid_act_scores([27, 32, 36, 48, 0, 29]))

