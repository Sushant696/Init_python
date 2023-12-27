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

# 7. reverse a list

# mylist = [1,2,3,5]
# i = 0 
# reversed_list =[]

# while (i < len(mylist)):
#     print('hello')
#     reversed_list = mylist[::-1]
#     i += 1 
# print(reversed_list)

# given list is [1,2,3,4] but expected output in new list [2,3,4,5]

# mylist = [1,2,3,4]
# newList = []
# i = 0 
# while i < len(mylist):
#     if (mylist[i]== 1):
#         i += 1
#         continue
#     else:
#         newList.append(mylist[i])
#     if (mylist[i]==4):
#         newList.append(5)
#     i += 1
# print(newList)


# 9. Given list is lst=[1,2,3,4] but print 1 and 4 only 

# mylist = [1,2,3,4]
# # print 1 , 4 
# i = 0 
# while i < len(mylist):
#     if mylist[i] == 1 or mylist[i]== 4 :
#         print(mylist[i])
#     i +=1

# 15. Python program that accepts a string and calculate the number of digits and letters and space

# 16. Python program to check the validity of username and password input by users

# else with while 

# i =0 
# while i < 5 :
#     if i == 3 :
#         i += 1
#         continue
#         print(i)
#     i = i + 1
#     else :
#         print('end of loop')


# i = 0 
# while i < 5 :
# if i == 


result = 1
i = 8
while i >= 2:
    j = 1
    while j <= 10 :
        result = i *j
        print(f'{i} * {j} = {result}')
        j +=1
    # result = i
    print('\n')
    i -=1


