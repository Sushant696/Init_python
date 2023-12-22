# lets learn about while loop making an simple guessing game
# import random
# guess_left = 3
# random = random.randint(0, 9)
# i = 1

# while guess_left > 0:
#     userInput = int(input('Enter you guess from 1 - 9: '))

#     if (random == userInput):

#         print("You made the right guess")
#         break

#     elif (random < userInput):

#         print('Your guess is high, try again with lower value')

#     elif (random > userInput):

#         print("Your guess is low , try again with higher value")

#     else:

#         print('your guess is wrong', f"only {guess_left} gueses left!")

#     guess_left -= 1


# using while loop 
# a = 0 
# print("hello")
# b = 'softwarica'
# while (a < 10):
#     print(b[a])
    # a +=1

# multiplication table using while loop

# a = 1
# result = 1
# while (a <= 10):
#     result = 2 * a
#     print(f"2 * {a} = {result} ") 
#     a  += 1 


# a = [1,2,3,4,5]
# i = 0 
# len1 = len(a)
# product = 1 

# while (i < len1):
#     product *= a[i]
#     print(f"2 * {a} = {result} ")

#     i += 1
    
# a = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
# index = 0
# while index < len(a):
#     if isinstance(a[index], int):
#         print(a[index])
#     index += 1


# a = [1, 2, 3, 4, 'a', 'b', 'c', 'd']
# string = []
# num = []

# index = 0
# while index < len(a):
#     if isinstance(a[index], int):
#         num.append(index)
#     index += 1

# print(num)


# carefull with continue in while loop (infinite loops)