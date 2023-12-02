import random
from stages import logo
from words import word_list
from stages import stages

name = input('Enter your game name:')
print(f'{logo}\nWelcome to the Hangman Game!!')
print(f"HI! {name} Let's begin the game")

random.shuffle(word_list)
random.shuffle(word_list)
random.shuffle(word_list)
chosen_word = random.choice(word_list)
# print('The number you have to guess is:', chosen_word)
display = ['_']*len(chosen_word)
print(
    f'The word consist of {len(chosen_word)} letters it\'s first letter is {chosen_word[0]}')
print(display)
chosen_word.lower()

min_attempts = 0
max_attempts = 6

while max_attempts >= min_attempts:
    letter_in_word = False

    # word verification
    user_guess = input("Guess the letter ").lower()
    if len(user_guess) != 1 or not user_guess.isalpha():
        print("please enter a single letter: ")
        continue

    # guessing the letter
    for i in range(len(chosen_word)):
        if user_guess == chosen_word[i]:
            display[i] = user_guess
            letter_in_word = True


    # loosing condition
    if min_attempts == max_attempts:
        print(stages[min_attempts])
        print(f"You lost, Try again. The correct word was {chosen_word}")
        break

    # letter present or not
    if letter_in_word:
        print(display)

    else:
        print(stages[min_attempts])
        print(display)
        print(
            f'sorry, the letter doesn\'t match  {max_attempts - min_attempts} tries left \n')
        min_attempts += 1

    # winning condition
    if '_' not in display:
        print('congratulations, You won the game')
        break