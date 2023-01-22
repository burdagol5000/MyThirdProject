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
    displayed_word=len(chosen_word)
    for letter in displayed_word:
        print('_', end=' ')
        print(letter)

def category_selection():
    chosen_category = int(input("Choose your Category: "))
    category_words=random.chosen_category=(words[chosen_category])
    chosen_word=random.choice(category_words)
try:
    category_selection()
    the_game(chosen_word)
except ValueError:
    print("Please Select from the correct category!!")
    category_selection()
    the_game(chosen_word)

except IndexError:
    print("Please Select from the correct category!!")
    category_selection()
    the_game(chosen_word)

except NameError:
    print("Please Select from the correct category!!")
    category_selection()
    the_game(chosen_word)


