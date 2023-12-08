# userInput = int(input('enter you number'))

# 1

# if (userInput % 2 == 0):
#     print('The number you entered in even')
# else:
#     print('The number you entered is odd')


# 2

# student_marks = eval(input('Enter your marks'))
# if (student_marks >= 80 and student_marks <= 100):
#     print("you got A")
# elif (student_marks >= 60 and student_marks <= 80):
#     print('you got b')
# elif (student_marks >= 50 and student_marks <= 60):
#     print('you got c')
# elif (student_marks >= 45 and student_marks <= 50):
#     print('you got d')
# elif (student_marks >= 25 and student_marks <= 45):
#     print('you got e')
# elif (student_marks <= 25):
#     print('you got f')
# else:
#     print('please enter valid marks')


# 3 n for n

# m = eval (input('enter number '))
# if (m > 0):
#     n = 1
#     print(f"m greater than 0 then n = {n}")
# elif (m == 0):
#     n  = 0
#     print(f"m equalls to 0 than n  = {n}")
# elif (m  < 0):
#     n = -1
#     print(f"m is less  n ={n}")

# 4 are both equall 
# num1 = eval(input("Input first number "))
# num2 = eval(input("Input second number "))

# if (num1 == num2):
#     print('Both numbers are equall')
# else :
#     print('The numbers are not equall')

# 5 positive or negative 

# num = eval(input('Enter a number :'))
# if (num > 0):
#     print('The number is positive')
# elif(num < 0):
#     print("The number is even")
# else:
#     print('please enter a valid integer')

# 6 find the largest number 

# num1 = eval(input('enter a number'))
# num2 = eval(input('enter a number'))
# num3 = eval(input('enter a number'))

# if (num1>num2 and num1>num3):
#     print('The num1 = %s is the greatest of all' %(num1))
# elif(num2 > num1 and num2 > num3):
#     print(f"The num2 = {num2} is the greatest of all")
# elif(num3 > num1 and num3 > num2):
#     print('The num 3  = {} is the greatest'.format(num3))

# 7 digit or a alphabet 

# userIput = input('enter a character: ')

# if (int(userIput.isalpha())):
#     print('the user input is alphabet')
# elif(userIput.isdigit()):
#     print("The number is a digit")
# else :
#     print('enter a valid character')


# 8
# vovel= 'aeiou'
# consonant = "bcdfghjklmnpqrstvwxyz"
# userInput = input('enter a alphabet from a-z')
# if (userInput in vovel):
#     print('the alphabet is a vovel')
# elif(userInput in consonant):
#     print('The alphabet is consonant')
# else:
#     print('enter a valid alphabet')

# 9> divisible by 3
# num = eval(input('Enter a number '))

# if (num % 3 == 0):
#     print('The userinput is divisible by 3')
# else :
#     print("The userInput is not divisible by 3")


# 10 multiple of 5 
# num = eval(input('Enter a number '))

# if (num % 5 == 0):
#     print('hello')
# else :
#     print("bye")



# 11 get a day of the week by entering 1-7

# user_input = int(input('enter 1-7 to get the day'))

# if(user_input == 1):
#     print('sunday')
# elif (user_input == 2):
#     print("monday")
# elif(user_input== 3):
#     print('tuesday')
# elif(user_input== 4):
#     print('wednesday')
# elif(user_input== 5):
#     print('thursday')
# elif(user_input== 6):
#     print('friday')
# elif(user_input== 7):
#     print('saturday')
# else :
#     print("please input numbers from 1-7")



# 12 display a month in sequence
# user_input = int(input('enter 1-7 to get the day'))

# if(user_input == 1):
#     print('january')
# elif (user_input == 2):
#     print("february ")
# elif(user_input== 3):
#     print('march')
# elif(user_input== 4):
#     print('april')
# elif(user_input== 5):
#     print('may')
# elif(user_input== 6):
#     print('june')
# elif(user_input== 7):
#     print('july')
# else :
#     print("please input numbers from 1-7")



# 13 user_input = input('Enter a city name')

# match user_input :
#     case  'agra':
#         print(f'Most visit monument in {user_input} is red fort ')
#     case  'delhi':
#         print(f'Most visit monument in {user_input} is taj mahal')
#     case  'jaipur':
#         print(f'Most visit monument in {user_input} is jal mahal')
#     case __ :
#         print("Invalid, Enter city name among agra , delhi and jaipur")



# 14
# num = int(input('Enter a number'))

# if (num % 2 == 0 and num %  3 == 0 ):
#     print('The number is divisible by 2')
# elif  (num % 3 == 0):
#     print('The number is divisible by 3')
# elif (num % 2 == 0):
#     print('The number is divisible by 2 and 3 both')
# else:
#     print("invalid number")


# 15
# num1 = eval(input('enter a number'))
# num2 = eval(input('enter a number'))
# num3 = eval(input('enter a number'))

# if (num1<num2 and num1num3):
#     print('The num1 = %s is the smallest of all' %(num1))
# elif(num2 < num1 and num2 < num3):
#     print(f"The num2 = {num2} is the smallest of all")
# elif(num3 < num1 and num3 < num2):
#     print('The num 3  = {} is the smallest'.format(num3))


# 16

# userInput == int(input('enter you age'))


# if (userInput > 18 ):
#     print('Dear user you are eliglible for voting')
# else:
#     print('You are not old enough to vote')




#  18
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter the operator: ")

if operator == "+":
    print(f"{num1} {operator} {num2} = {num1 + num2}")
elif operator == "-":
    print(f"{num1} {operator} {num2} = {num1 - num2}")
elif operator == "*":
    print(f"{num1} {operator} {num2} = {num1 * num2}")
elif operator == "/":
    print(f"{num1} {operator} {num2} = {num1 / num2}")
elif operator == "**":
    print(f"{num1} {operator} {num2} = {num1 ** num2}")
elif operator == "//":
    print(f"{num1} {operator} {num2} = {num1 // num2}")
else:
    print("invalid Mathematical Operator")



# Question 19
x = 1
if x > 0:
    print("True")
elif x < 0:
    print("False")
else:
    print("zero")


# 20
name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print(F"Your name is {name}\nYour age is {age}\nYour address is {address}")
