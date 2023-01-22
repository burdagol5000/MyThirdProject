import random 
name=input("Please Enter Your Name:")
print(f'Welcome to Guess the word!, {name}')
print("Please Choose your category:")
print("0.Animals")
print("1.Countries")
print("2.Gods and Goddesses")
words=[["elephant","rhinoceros","zebra","giraffe"],
["philippines","australia","russia","ukraine","ireland"],
["zeus","thor","odin","hermes","athena","ares","tyr"]]

def the_game(chosen_word): 
    lives=5
    incorrect_guess=[]
    correct_guess=[]
    answer=[]
    displayed_word=chosen_word
    for letter in displayed_word:
        if letter.isalpha():
            answer.append('_')
            correct_guess.append(letter)
        else:
            answer.append(letter)

    print("")
    while True:
        try:
            guess=str(input("Enter your Answer:"))
            
            if len(guess)!=1:
                print("Please enter 1 letter only!")
            if not guess[0].isalpha():
                print("Please Enter a Letter!")
            if guess in incorrect_guess:
                print("Letter has been selected already")
            if guess not in answer:
                incorrect_guess.append(guess)
                lives=lives-1
                print(incorrect_guess)
                for letter in displayed_word:
                    answer.append(letter)
                    print('_',end=' ')
            if lives==0:
                print("You Lose!")
                print(f"The Word is {chosen_word}")
                break
            if guess in answer:
                correct_guess.append(guess)
                print(correct_guess)
                for letter in displayed_word:
                    answer.append(letter)
                    print('_',end=' ')
        except ValueError:
            print("Enter a correct answer!")


def category_selection():
        chosen_category = int(input("Choose your Category: "))
        category_words=random.chosen_category=(words[chosen_category])
        chosen_word=random.choice(category_words)
        the_game(chosen_word)    
while True:
        try:
            category_selection()
        except ValueError:
            print("Please Select from the correct category!!a")
            category_selection()
        except IndexError:
            print("Please Select from the correct category!!b")
            category_selection()
        except NameError:
            print("Please Select from the correct category!!c")
            category_selection()

