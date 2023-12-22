# Solve these questions using both while loop and for loop


# 1. print "softwarica" 10 times

# name = 'softwarica'

# for i in range(1, 11):
#     print(i, name)


#2 add items of list
# mylist = [1, 2, 3, 4, 5]
# add = 0


# for i in mylist:
#     add += i
#     print(add)

#  print each character using indexing

# name = 'softwarica'
# length = len(name)

# for i in  range(length):
#     print(name[i])



# . write a program to display integer from of a list 
# lists=[1,"a","c",2,3,4]

# for i in lists :
#     if(isinstance(i, int)):
#         print(i , "is a int")



# 5. multiplication of a each element. given 

# lists=[4,5,3,2]
# multiply = 1

# for i in lists:
#     multiply *= i
#     print(multiply)


# 6 multiplication table of a given number 7
# number = 7 
# for i in range(1,11):
#     result = i * number 
#     print(f"{number}*{i}={result}")


# 7. reverse a list
# mylist = [1,2,4,5,1,7,74,8]
# reversed_list = mylist[::-1]
# print(mylist,reversed_list)

# 8 given list is [1,2,3,4] but expected output in new list [2,3,4,5]

# original_list = [1, 2, 3, 4]

# new_list = []

# for i in original_list:
#     print(i)
#     new_element = i + 1
#     new_list.append(new_element) # we are appending each element by looping through the loop i value is + 1 so from 2 to 5 are being appended

# print(new_list)

#9 Given list is lst=[1,2,3,4] but print 1 and 4 only 

# lst=[1,2,3,4] #print 1 and 4 

# for i in lst:
#     if(i==1 or i == 4):
#         print(i)


# 10. Given list is lst=[1,2,3,4] but print 1 2 and 4 only

# lst=[1,2,3,4] #print 1 ,2 and 4 

# for i in lst:
#     if(i==1 or i == 4 or i == 2):
#         print(i)

# 11. Given list is [1,2,3,4] but expected output is [1,"a",2,4]
# orgList = [1,2,3,4]

# for i in range(len(orgList)):
#     # manually 
#     if i == 1:
#         orgList[i] = "a"
#     elif i == 2:
#         orgList[i] = 2

# # Print the modified list
# print(orgList)

# 12. Given list is [1,2,3,4,5] separate the elements into odd and even categories.
# mylist = [1,2,3,4,5]
# odd = []
# even = []

# for i in mylist:
#     if (i % 2 == 0):
#         even.append(i)
#     else:
#         odd.append(i)

# print(odd , even)

# 13. Given list is [1,2,3,"d",4,5,"a"] separate the elements based on their data types

# mylist = [1,2,3,"d",4,5,"a"]
# integer = []
# strings = []
# for i in mylist:
#     if (isinstance(i,int)):
#         integer.append(i)
#     elif(isinstance(i,str)):
#         strings.append(i)

# print(integer,strings)

# 14. Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.

mylist = [1,2,3,4,"a","b"]
integer = []
strings = []
for i in mylist:
    if (isinstance(i,int)):
        integer.append(i)
    elif(isinstance(i,str)):
        strings.append(i)

print(f"integers = {integer}, strings = {strings}")

# 15. Python program that accepts a string and calculate the number of digits and letters and space


# user_input = input('enter a sting')

# for i in user_input:

    # if(i.isdigit):
