
# # # Open the source file for reading
# # source_file = open("b.txt", 'r')
# # file_contents = source_file.read()
# # source_file.close()

# # # Write the contents to the destination file
# # destination = open('a.txt', 'w')
# # destination.write(file_contents)
# # destination.close()

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

def reverseString(string, index):
    
    # base case 
    if index < 0:
        return string
    else:
        return string[index] + reverseString(string, index - 1)


userInput = input('Enter a string: ')
length = len(userInput)
index = length - 1
reverse = reverseString(userInput, index)
print(reverse)
