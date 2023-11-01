import random
guess = 0
count = 3
random = random.randint(0, 9)
print(random)
i = 1

while count > 0:
    userInput = int(input('Enter you guess'))
    if (random == userInput):
        print("You made the right guess")
        break
    else:
        print('your guess is wrong', f"{count}")
    count -= 1

# i made the number guessing game by myself without looking for external help here is my first success
