name=input("Please Enter Your Name:")
print(f'Welcome to Guess the word!, {name}')
print("Please Choose your category:")
print("0.Animals")
print("1.Countries")
print("2.Gods and Goddesses")
try:
   chosen_category=int(input("Choose your Category: "))
   
except ValueError: 
    clear()
    print("Please Select from the correct category")
    
words=[["elephant","rhinoceros","zebra","giraffe"],["philippines","australia","russia","ukraine","ireland"],["zeus","thor","odin","hermes","athena","ares","tyr"]]
random_word=random.chosen_category(words[chosen_category])
print(random_word)