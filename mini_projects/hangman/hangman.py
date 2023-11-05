import random
from stages import logo
print(logo)

# def welcome():
    # print('Welcome to the Hangman Game!,hangman_logo')
#     name = input()
#     print(f"HI!{name} Let's begin the game")
# welcome()

word_list = [
'python',
'absurd',
'nightclub',
'quantum',
'computer',
"function",
'jukebox',
'strength',
"conditional",
'krugger', 
'awareness',
"debugging",
'jiujitsu',
"database",
"optimization",
"framework",
"interface",
"authentication",
"version",
"iteration",
"repository",
"variable",
"authorization"

,]

# assign random word to the user
chosen_word = random.choice(word_list)
print('The number you have to guess is:',chosen_word)
display = ['_']*len(chosen_word)
print(display)


# check if that word has that letter 
# if the word has that letter then add that letter and display
# use the max and min attempts concept  

min_attempts = 0 
max_attempts = 6

while max_attempts >= min_attempts :
    guess = input("guess the letter").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("please enter a single letter:") 


    min_attempts +=1