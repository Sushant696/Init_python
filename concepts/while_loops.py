# lets learn about while loop making an simple guessing game
import random
guess_left = 3
random = random.randint(0, 9)
i = 1

while guess_left > 0:
    userInput = int(input('Enter you guess from 1 - 9: '))

    if (random == userInput):

        print("You made the right guess")
        break

    elif (random < userInput):

        print('Your guess is high, try again with lower value')

    elif (random > userInput):

        print("Your guess is low , try again with higher value")

    else:

        print('your guess is wrong', f"only {guess_left} gueses left!")

    guess_left -= 1

# i made the number guessing game by my self
