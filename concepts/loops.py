# let's dive deep into loops and continue loops evercise after all loops 

# loop through string and add those string to list as individual items 

# string = "python"
# lists = []
# for x in string: 
#     lists.append(x)
#     print(lists)


# find all the odd number from 1 to n 
# n = int(input("enter the number"))
# for x in range(1,n+2,5):
#     print(x)

# print(range(5)) # range(0,5)

# using brake statements
# fruits = ["apple",'mango','strawberry','banana','cherry']
# for i in fruits:
#     print(i)
#     if i == "mango":
#         break

# Note : the else will not be executed if the loop is stopped by a break statement

# continue in python
# for i in range (8):
#     if i == 3:
#         continue 
#     print(i)

# skip the iteration if i == 3  and continue with next iteration 


# nested loops in python
# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in range(3): 
#     for y in fruits:
#         print(x,y)
    

# the inner loop will be executed one time for each iteration of the outer loop 

# pass statement does nothing but you can use pass to avoid getting error due to empty loops or conditionals

# write a program to take an word from user and reverse it 

# n = input("Enter a word you want to reverse  ")

# a = n[::-1]
# print(a)

# Write a Python program that iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for multiples of five print "Buzz". For numbers that are multiples of three and five, print "FizzBuzz".

# for i in range(51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("fizzBuzz")
#     elif i % 3 == 0 :
#         print("fizz")
#     elif i % 5 == 0 :
#         print("Buzz")
#     else:
#         print(i)


# Write a Python program to check the validity of passwords input by users.
# Validation :

# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.