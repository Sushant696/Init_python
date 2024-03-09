
# # Open the source file for reading
# source_file = open("b.txt", 'r')
# file_contents = source_file.read()
# source_file.close()

# # Write the contents to the destination file
# destination = open('a.txt', 'w')
# destination.write(file_contents)
# destination.close()

# # print("File copy successful.")
# # How to remove a dictionary key and change value in a dictionary.


# mydict = {"key" : "value zero", "key1" : 'value one'}
# # removing an item form the dictionary...
# mydict.pop("key")
# # changes the value using an key
# mydict["key"] = 'new updated value'
# print(mydict)


# write a program to display if the entered number is armstrong or not??

# user_input = int (input("Enter a number"))
# user_input_copy = user_input

# sum = 0
# while user_input_copy > 0:

#     r = user_input_copy % 10
#     sum +=  r ** 3
#     user_input_copy //= 10
#     print(r,user_input_copy,sum)

# if user_input == sum:
#     print("The number is armstrong..")
# else :
#     print('the number is not armstrong')


# reverse a string using recursion

# string = 'hello this is a string'
# length = len(string)
# index = length -1
# reversed_str= ''


# while index >= 0:
#     reversed_str += string[index]
#     index -=  1

# print('og =',string,reversed_str)


# now let's use recursion

# def reverseString(string, index):

#     # base case
#     if index < 0:
#         return string
#     else:
#         return string[index] + reverseString(string, index - 1)


# userInput = input('Enter a string: ')
# length = len(userInput)
# index = length - 1
# reverse = reverseString(userInput, index)
# print(reverse)

# numbers = [1, 2, 3, 4, 5, 6]
# doubled_odd_numbers = [num * 2 for num in numbers if num % 2 == 0]
# print(doubled_odd_numbers,numbers)


# Write a function words() in python to read lines from a text file "story.txt", and display those words, which are less tha 4 charaters.


# we have to store the content using read and also assign it to a variable so see it's result


# copy content of one file to another

# file = open('a.txt', 'r')
# file_contents = file.read()
# print(file_contents)
# file.close()

# file1 = open("c.txt", 'w+')
# file1.write(f"{file_contents}")
# file1.close()


# with open('a.txt', 'r') as file:
#     file_contents = file.read()
#     print(file_contents)

# with open('c.txt', 'w+') as file1:
#     file1.write(file_contents)


# what is lambda function how to use in python 

a =2
b=9
square = lambda a,b : a**b 
print(square(a,b))