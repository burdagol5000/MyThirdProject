import random 
name=input("Please Enter Your Name:")
print(f'Welcome to Guess the word!, {name}')
print("Please Choose your category:")
print("0.Animals")
print("1.Countries")
print("2.Gods and Goddesses")
try:
   chosen_category=int(input("Choose your Category: "))
except ValueError:
    print("Please Select from the correct category")
except IndexError:
    print("Please Select from the correct category")
except NameError:
    print("Please Select from the correct category")

if chosen_category > len(2):
            clear()
            print("No such topic!!! Try again.")
        elif chosen_category == len(2):
            print()
            print("Thank you for playing!")
            break
words=[["elephant","rhinoceros","zebra","giraffe"],["philippines","australia","russia","ukraine","ireland"],["zeus","thor","odin","hermes","athena","ares","tyr"]]
category_words=random.chosen_category=(words[chosen_category])
game=random.choice(category_words)
print(game)