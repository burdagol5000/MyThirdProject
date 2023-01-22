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
def category_selection():
    chosen_category = int(input("Choose your Category: "))
    category_words=random.chosen_category=(words[chosen_category])
    game=random.choice(category_words)
    print(game)
try:
    category_selection()
except ValueError:
    print("Please Select from the correct category!!")
    category_selection()
except IndexError:
    print("Please Select from the correct category!!")
    category_selection()
except NameError:
    print("Please Select from the correct category!!")
    category_selection()

