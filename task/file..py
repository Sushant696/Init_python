

###########################################################################

# Python code to copy content of one file to another


# # Open the source file for reading
# source_file = open("a.txt", 'r')
# file_contents = source_file.read()
# source_file.close()


# # Write the contents to the destination file
# destination = open('b.txt', 'w+')
# destination.write(file_contents)
# destination.seek(0)
# data = destination.read()
# print(data)
# destination.close()


# another = open("b.txt",'r')
# contents = another.read()
# print(contents,'file contents')
# another.close()


# 34. Write a function “words()” in python to read lines from a text file "story.txt", and display
# those words, which are less than 4 characters.

# def word():
#     with  open('a.txt',"r+") as filename:
#         lines = filename.readlines()
#         print(lines)
#     for line in lines:
#         words = line.split()

#         for word in words:
#             if len(word) < 4:
#                 print(word)
# word()


# def words_print():
#     with open('a.txt', "r+") as filename:
#         lines = filename.readlines()
#         words = []
#         for line in lines:
#             words += line.split()
#         for word in words:
#             if len(word) <= 4:
#                 print(word)


# # Call the function
# words_print()

# How will you remove duplicate elements from a list...

# list1 = [1,1, 2, 3, 2, 1,1, 4]
# index = len(list1) - 1

# for i in range(index):
#     for j in range(i + 2, index):
#         if list1[i] == list1[j]:
#             list1.pop(j)
#             index -= 1
# print(list1)




list1 = [1, 2, 3, 2, 1, 1, 4]
newList = []

for i in list1:
    if i not in newList:
        newList.append(i)

print(newList)


