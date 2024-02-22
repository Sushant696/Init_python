# # wap to find factorial of a number using while loop

# fact = 1 
# num = int (input('Enter a number'))

# for i in range(1,num+1):

#     fact *= i

# print(fact)



# Wap to find the sum of all number stored in a list using for loop and while loop

#                        ------- using for loop ---------- 


# myList = [3,4]
# sum = 0

# for i in range(len(myList)):
#     sum += myList[i]
# print(sum)
#                        ------- using while loop ---------- 

myList = [3,4,23]

sum = 0 
i = len(myList) - 1 
while i >= 0 :

    sum += myList[i]
    i -= 1
print(sum)