# 1. Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".

# a = eval(input('Enter a number'))
# b = eval(input('Enter another number :'))


# if(a==b):
#     print('1')
# elif(a>b):
#     print('2')
# else:
#     print("3")

# 2 Print "Hello" if a is equal to b, or if c is equal to d.

# a = int(input('enter first number'))
# b = int(input('enter second number'))
# c = int(input('enter third number'))
# d = int(input('enter forth number'))

# if (a == b or c == d):
#     print('Hello')
# else :
#     print('a != b and c != d')


# 3 Print "Hello" if a is equal to b, and c is equal to d.
# a = int(input('enter first number'))
# b = int(input('enter second number'))
# c = int(input('enter third number'))
# d = int(input('enter forth number'))

# if (a == b and c == d):
#     print('Hello')
# else :
#     print('a != b and c != d')


# 4 For given integer x, print ‘True’ if it is positive, print ‘False’ if it is negative and print ‘zero’ if it is 0.

# x = int(input('Enter a number '))

# if(x > 0):
#     print('positive')
# elif(x < 0):
#     print('Negative')
# else:
#     print("The numeber is zero")

# 5  Check whether the user input number is even or odd and display it to user.

# userInput = int(input('enter you number'))

# if (userInput % 2 == 0):
#     print('The number you entered in even')
# else:
#     print('The number you entered is odd')


# # 6 WAP which accepts marks of four subjects and display total marks, percentage and grade
# # Hint: more than 70% –> distinction, more than 60% –> first, more than 40% –> pass,less than 40% –> fail

# # Input from student

# maths = int(input("Maths marks"))
# programming= int(input("programmingmarks"))
# softwareDesign = int(input("softwareDesign marks"))
# Nepali = int(input("Nepali marks"))


# # Variable for programs

# totalMarks = 400
# Obtained_marks = maths + programming + softwareDesign + Nepali
# percentage = (Obtained_marks / totalMarks) * 100
# distinction = percentage > 70

# print(f"total marks : {totalMarks}, obtainded marks:{Obtained_marks},percentage:{percentage}")

# contition to know grade of the student

# if (distinction):
#     print(f'distinction with {percentage}%')
# elif(percentage > 60 and percentage < 70):
#     print(f'first division with {percentage}%')
# elif(percentage > 40 and percentage < 60):
#     print(f'pass with {percentage}%')
# elif(percentage < 40 and percentage >= 0):
#     print("fail")
# else:
#     print('Error occured')


# 7 What is the output of ‘APPLE’ > ‘apple’?

# a = 'apple'
# b = "APPLE"
# c = a > b
# print(c)


# 8. Write a program to accept the cost price of a bike qnd display the road tax to be paid according to the following criteria:
# Cost price(in Rs)                  Tax
# >100000                              15%
# >50000 and <=100000      10%
# <=50000                               5%


# cp = int(input('enter cp'))


# if (cp > 1000000):
#     tax = 15
#     tax_amt = 15 /100 * cp
#     print(f"road tax for{cp} is {tax_amt}")

# elif (cp > 50000 and cp <= 100000):
#     tax = 10
#     tax_amt = 10 /100 * cp
#     print(f'road tax for{cp} is {tax_amt} ')
# elif (cp <= 50000):
#     tax = 5
#     tax_amt = 5 / 100 *cp
#     print(f"road tax for{cp} is {tax_amt}")
# else :
#     print("enter a valid number")


# 9. Accept the age of 4 people and display the youngest one.

# a = int(input("Enter your age"))
# b = int(input("Enter your age"))
# c = int(input("Enter your age"))
# d = int(input("Enter your age"))


# if(a > b and a > c and a > d ):
#     print('a is the greatest')
# elif(b > a and b > c and b > d ):
#     print('b is the greatest among all')
# elif(c > a and c > b and c > d ):
#     print('c is the greatest among all')
# elif (d > a and d > b and d > c):
#     print('d is the greatest among all')


# 10. Accept the age of 4 people and display the oldest one.

# a = int(input("Enter your age"))
# b = int(input("Enter your age"))
# c = int(input("Enter your age"))
# d = int(input("Enter your age"))


# if(a < b and a < c and a < d ):
#     print('a is the smallest')
# elif(b < a and b < c and b < d ):
#     print('b is the smallest among all')
# elif(c < a and c < b and c < d ):
#     print('c is the smallest among all')
# elif (d < a and d < b and d < c):
#     print('d is the smallest among all')


# 11. Accept the percentage from the user and display the grade according to the following criteria:
# Below 25 --D
# 25 to 45  -- C
# 45 to 50 -- B
# 50 to 60 --B+
# 60 to 80 -- A
# Above 80 -- A+

# percentage = eval(input('Enter your percentage'))
# if (percentage >= 80 and percentage <= 100):
#     print("you got A+")
# elif (percentage >= 60 and percentage <= 80):
#     print('you got A')
# elif (percentage >= 50 and percentage <= 60):
#     print('you got B+')
# elif (percentage >= 45 and percentage <= 50):
#     print('you got B')
# elif (percentage >= 25 and percentage <= 45):
#     print('you got c')
# elif (percentage <= 25):
#     print('you got d')
# else:
#     print('please enter valid percentage')


# 12. A company decided to give bonus to employee according to following criteria:
# Time period of service     Bonus
# More than 10 years            10%
# >=6 and <=10                       8%
# Less than 6 years                 5%

# experience = int(input("enter your time period of service"))

# if (experience > 10):
#     print('you will get bonus of 10%')
# elif(experience >= 6 and experience <= 10):
#     print('you are eligible for 8%\ bonus')
# elif(experience < 6):
#     print('you are eligible for 6%\ bonus')
# else:
#     print('enter a valid option')

# 13 14. Accept the number of days from the user and calculate the charge for library according to following:
# Till five days: Rs 2/day
# Six to ten days: Rs 3/day
# 11 to 15 days: Rs 4/day
# After 15 days: Rs 5/day

# change to charge according to the days and use that in you code that way no need to hard code
# days = int(input("Enter number of days"))
# charge = 0
# if (days < 5):
#     charge = 2 * days
# elif(days> 6 and days <= 10):
#     charge = 3 * days
# elif (days>11 and days < 15):
#     charge = 4 * days
# elif(days > 15):
#     charge = 5 * days
# else:
#     print("invalid input")

#  Write a program to check two strings are anagram or not.
# string1 = input('enter first string: ')
# string2 = input('enter seccond string: ')
# # print(len(string1))


# def anagram(str1, str2):
#     if (len(string1) != len(string2)):
#         print("The string are not annagram: ")
#     a = sorted(str1)
#     b = sorted(str2)
#     if (a == b):
#         print(f'the words {string1} , {string2} is anagram ')
#     else:
#         print("the two strings are nots same!!!")


# anagram(string1, string2)


# 31. Accept the age, sex('M', 'F'), number of days and display the wages accordingly.
# Age                       Sex    Wage/day
# >=18 and <30      M        700
#                               F         750
# >=30 and <=40    M        800
#                               F         850

# age = int(input("Enter a number"))
# sex = input("Enter a sex")
# days = int(input("no of days"))
# wages = 0 


# if(sex== "male"):
#     male()
# elif(sex== "female"):
#     female()

# def male():
#     pass

# def female():
#     pass 



