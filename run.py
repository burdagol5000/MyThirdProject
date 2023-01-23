# importing the random and os module
import random
import os

# getting users name and welcome message
name = input("Please Enter Your Name:")
print("====================================")
print(f'Welcome to Guess the word!, {name}')
print("====================================")
words = [["elephant", "rhinoceros", "zebra", "giraffe"],
         ["philippines", "australia", "russia", "ukraine", "ireland"],
         ["zeus", "thor", "odin", "hermes", "athena", "ares", "tyr"]]


# the main function that will run the game
def the_game(chosen_word):
    lives = 5
    incorrect_guess = []
    correct_guess = []
    answer = []
    displayed_word = chosen_word
    # displaying the number of letters player need to guess
    for letter in displayed_word:
        if letter.isalpha():
            correct_guess.append("_")
            answer.append(letter)
        else:
            correct_guess.append(letter)
    print(correct_guess)
    while True:
        try:
            guess = str(input("Enter your Answer:"))
            # validation for user to input the correct characters
            if len(guess) != 1:
                print("Please enter 1 letter only!")
                continue
            if not guess[0].isalpha():
                print("Please Enter a Letter!")
                continue
            if guess in incorrect_guess:
                print("Letter has been selected already")
                continue
            # checking for users input
            if guess not in answer:
                incorrect_guess.append(guess)
                lives = lives-1
                print(f"Incorrect: {incorrect_guess}")
                for item in range(len(answer)):
                    if displayed_word[item] == guess:
                        correct_guess[item] = guess
                print(correct_guess)
            if lives == 0:
                print("You Lose!")
                print(f"The Word is {chosen_word}")
                new_game()
            if guess in answer:
                print(f"Incorrect: {incorrect_guess}")
                for item in range(len(answer)):
                    if displayed_word[item] == guess:
                        correct_guess[item] = guess
                print(correct_guess)
            if correct_guess == answer:
                print("Congratulations you have the correct answer")
                print(f"The word is {displayed_word}")
                new_game()
        except ValueError:
            print("Enter a correct answer!")


# function for starting a new game after finishing
def new_game():
    new = str(input("Start a new game? Y=Yes  N=No, Exit :").upper())
    if new == "Y":
        category_selection()
    if new == "N":
        exit()
    if not new.isalpha():
        print("Please Enter a Letter!")
        new_game()
    if new != "Y" or "N":
        print("Please Enter just Y or N")
        new_game()


# function for the selection of the category
def category_selection():
    print("Please Choose your category:")
    print("0.Animals")
    print("1.Countries")
    print("2.Gods and Goddesses")
    try:
        chosen_category = int(input("Choose your Category: "))
        category_words = random.chosen_category = (words[chosen_category])
        chosen_word = random.choice(category_words)
        the_game(chosen_word)
    except ValueError:
        print("Please Select from the correct category!!a")
        category_selection()
    except IndexError:
        print("Please Select from the correct category!!b")
        category_selection()


category_selection()
