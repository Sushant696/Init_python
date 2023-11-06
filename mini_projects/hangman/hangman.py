import random
from stages import logo
from words import word_list
from stages import stages


# print(f'{logo}\nWelcome to the Hangman Game!!')
#name = input()
#print(f"HI!{name} Let's begin the game")




chosen_word = random.choice(word_list)
print('The number you have to guess is:',chosen_word )
display = ['_']*len(chosen_word)
print(display) 
chosen_word.lower()


# check if that word has that letter 
# if the word has that letter then add that letter and display
# use the max and min attempts concept  

min_attempts = 0 
max_attempts = 6

while max_attempts >= min_attempts :
    # word verification
    user_guess = input("Guess the letter ").lower()
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("please enter a single letter: ")
        continue

    



    # for i in chosen_word:
    #     if user_guess == i :
    #         display.append(user_guess)
    #         print(display)

# match the user's current guess with the letters present in word if matched then append it but how to know the index of that letter . need some sort of counter 



    print(stages[min_attempts])
    print(display)
    min_attempts +=1