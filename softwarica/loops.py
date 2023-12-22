# # Exercise 6: Count the total number of digits in a number
# # number = int(input('Enter a number'))
# # count = 0

# # while(number > 0):
# #     number = number // 10 
# #     count += 1 
# #     print(number)
# # print(f'the number of the digit is {count}')    

# # Exercise 10: Use else block to display a message “Done” after successful execution of for loop

# # for i in range(0,7,2):
# #     print(i)
# # else:
# #     print('Done')

# # # Exercise 11: Write a program to display all prime numbers within a range

# # prime = []
# # n = int(input("take the range of numbes"))
# # flag = 0

# # for i in range(2 , n + 1):
# #     if i > 1 :

# #         print('No prime number identified')
# #         if(i % 2 != 0):
# #             flag = 1
# #     if (flag == 1):
# #         print(f'{i} is prime number')
# #         prime.append(i)
# #     else:
# #         print(f"{i} is not a prime number")

# # print(prime)

# # prime = []
# # n = int(input("Enter the range of numbers: "))
# # flag = 0

# # for i in range(2, n + 1):
# #     if i > 1:
# #         flag = 1
# #         for j in range(2, int(i/2) + 1):
# #             if (i % j) == 0:
# #                 flag = 0
# #                 break
# #         if flag == 1:
# #             print(f'{i} is a prime number')
# #             prime.append(i)
# #         else:
# #             print(f"{i} is not a prime number")

# # print("Prime numbers within the range:", prime)



# # for i in range(11):
# #     result = 2 * i
# #     print(f'2 * {i}={result}')
# # Display the 2 times table

# # for i in range(-1, -11):
# #     result = 2 * i
# #     print(f'2 * {i} = {result}')

# # for i in range(10,0,-1):
# #     result = 2 * i
# #     print(f'2 * {i} = {result}')


# # add items of list
# # mylist = [1,2,3,4,5]
# # add = 0 
# # multiply = 1

# # for i in mylist:
# #     add += i 
# #     multiply *= i
# #     print(add , multiply)


# # mylist = [1,2,3,4,5]

# # odd =[]
# # even=[]

# # for i in mylist:
# #     if(i%2==0):
# #         print('even')
# #         even.append(i)
# #     else:
# #         print('odd')
# #         odd.append(i)
# # print(odd , even)


# mylist = ['a','b',1,2]

# for i in mylist:
#     print(f"{i} is of {type(i)}")
