import random

def number_guesser():
    secret1 = random.randint(1, 10)
    guess1 = ""
    lives = 2
    lives = int(lives)
    print("NUMBER_GUESSER")
    print("Guess the secret number")
    guess1 = input()
    while int(guess1) != secret1:
        if guess1 in "1,2,3,4,5,6,7,8,9,10":
            if int(guess1) > secret1:
                print("Too high")
                print("Guess Again")
                guess1 = input()
            elif int(guess1) < secret1:
                print("Too low")
                print("Guess Again")
                guess1 = input()
        else:
            print("Invalid input")
            print("Enter a number between 1-10")
            guess1 = input()

    if int(guess1) == secret1:
        print("You got it!")


def number_guesser_with_lives():
    secret2 = random.randint(1, 10)
    print("NUMBER_GUESSER_WITH_LIVES")
    print("Guess the secret number")
    guess2 = input()
    lives = 2
    lives = int(lives)
    while int(guess2) != secret2 and lives != 0:
        if guess2 in "1,2,3,4,5,6,7,8,9,10":
            if int(guess2) > secret2:
                lives = lives - 1
                print("Too high")
                print("Guess Again")
                guess2 = input()
            elif int(guess2) < secret2:
                lives = lives - 1
                print("Too low")
                print("Guess Again")
                guess2 = input()
        else:
                print("Invalid input")
                print("Enter a number between 1-10")
                guess2 = input()
    if int(guess2) == secret2:
        print("You got it!")
    else:
        print("Game Over")


def vending_machine():
    print("VENDING_MACHINE")
    due = 50
    due = int(due)
    while due > 0:
        print("Amount Due: ", due)
        coin = input("Insert Coin: ")
        if int(coin) in [10, 5, 25]:
            due = due - int(coin)
        else:
            due = due
    if due < 0:
        print("Change given:", due * -1)
    else:
        print("Change given:", 0)


def hangman():
    lives = 3
    wordlist = ["elephant", "pixie", "table", "hollow"]
    secret = random.choice(wordlist)
    guessed_count = 0
    guessed = False
    already_guessed = []
    while guessed == False and lives != 0:
        for letter in secret:
            if letter in already_guessed:
                print(letter, end="")
            else:
                print(" _ ", end="")
        print(" Guess a letter")
        guess = input()
        if guess in already_guessed:
            print("You Already Tried That Letter")
        if guess in secret:
            already_guessed.append(guess)
            guessed_count = guessed_count + secret.count(guess)
        else:
            print("INCORRECT")
            lives = lives - 1
        if guessed_count == len(secret):
            guessed = True
        else:
            pass
    if guessed == True:
        print("You Guessed the Word!!!")
        print("The Word Was:", secret)
    elif lives == 0:
        print("You Failed...")
        print("The Word Was:", secret)
hangman()