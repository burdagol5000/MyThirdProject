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
        answer.append(letter)
        print('_', end=' ')

        print("")
    while True:
        try:
            guess=str(input("Enter your Answer:"))

            if len(guess)!=1:
                print("Please enter 1 letter only!")
            if not guess[0].isalpha():
                print("Please Enter a Letter!")
            elif guess in incorrect_guess:
                print("Letter has been selected already")
            elif guess is not answer:
                incorrect_guess.append(guess)
                lives-=1
            elif lives == 0:
                print("\tGAME OVER!!!")
                print_hangman(hangman_values)
                print("The word is :", word.upper())
        except ValueError:
            print("Enter a correct answer!")

      

if __name__ == "__main__":
    def category_selection():
        chosen_category = int(input("Choose your Category: "))
        category_words=random.chosen_category=(words[chosen_category])
        chosen_word=random.choice(category_words)
        the_game(chosen_word)    
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

