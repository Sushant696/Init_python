import random
from stages import logo
from words import word_list
print(logo)

# def welcome():
    # print('Welcome to the Hangman Game!,hangman_logo')
#     name = input()
#     print(f"HI!{name} Let's begin the game")
# welcome()


# assign random word to the user

chosen_word = random.choice(word_list)
print('The number you have to guess is:',chosen_word )
display = ['_']*len(chosen_word)
print(display) 
chosen_word.upper()


# check if that word has that letter 
# if the word has that letter then add that letter and display
# use the max and min attempts concept  

min_attempts = 0 
max_attempts = 6

while max_attempts >= min_attempts :
    # word verification
    guess = input("Guess the letter ").upper()
    if len(guess) != 1 or not guess.isalpha():
        print("please enter a single letter: ") 
    else:
        print("not a valid guess")
    print(display)


    
#   current guess has the letter in it ? 
# chosen_word is full word and guess just has one letter so we should put the chosen word inside of the loop
    for i in chosen_word:
        if (guess == i):
            chosen_word.join(i)
            print(guess)


    min_attempts +=1