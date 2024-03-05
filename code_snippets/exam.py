# # num=4
# # def factorial (num):
# #    fact=1
# #    for i in range(1, num+1):
# #        fact-fact*1
# #    print(fact)
# # num-5
# # print (factorial (num))

# def prime_number(num):
#     '''
#     This Function checks if number is prime or not

#     args,
#     num : number to be checked

#     returns,
#     True is the numbers is prime, otherwise false
#     '''
#     if (num <= 2):
#         print("Please enter number greater than 2")
#         return False

#     flag = -1
#     for i in range(3, num):
#         if num % i == 0:
#             flag = False
#             return flag

#         else:
#             flag = True

#     return flag


# user_input = int(input("Enter a number:"))
# returned_value = prime_number(user_input)

# if (returned_value):
#     print('The number is a prime')
# else:
#     print('The number is not prime')


# user_input = input("please enter a sting: ")
# digitCount = 0
# spaceCount = 0
# letterCount = 0

# for i in user_input:
#     if i.isdigit():
#         digitCount +=1
#     elif i.isspace():
#         spaceCount +=1
#     elif i.isalpha():
#         letterCount += 1



# print(f"digit = {digitCount} \n space = {spaceCount} \n letter = {letterCount}")

lst = [11,32,-19,92,-83,189,-1]
lst1 = []

for i in lst:
    if i >= 0 :
        lst1.append(i)
print(lst1)