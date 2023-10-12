# print first 10 natural number using while loop 
# n = int (input("Enter the number:"))

# i = 1
# while i in range(n):
#     print(i)
#     i += 1

# print a triangle pattern using nested loop 
# count = 5
# for i in range(1,count + 1 , 1):
#     for j in range(1,i+1):
#         print(j ,end=' ')
#         count += 1 
#     print("\n")

# so how is this working is that
# first the count variable means number of rows that  triangle will have
# following that , the outer loop is printing the numebr of rows 
# After that , the innermost loop is executed one full iteration when the outer loop has done single iteration 

# will look at it tommorrow 

# 3  Calculate the sum of all numbers from 1 to a given number
# n = int(input("Enter the number"))
# add = 0 
# for i in range (n+1):
#     add = add + i 
# print(add)

# nested loops concept check again
# for i in range(7):
#     for j in range(i):
#         print("n",end= "_")
#     print('\n')

# print the pyramid
# rows = int(input("Enter number of rows: "))

# k = 0

# for i in range(1, rows+1):
#     for space in range(1, (rows-i)+1):
#         print(end="  ")
   
#     while k!=(2*i-1):
#         print("* ", end="")
#         k += 1
   
#     k = 0
#     print()



# print the floyds triangle
count = 0 
for i in range (3):
    for j in range (i+1):
        print(count,end= "")
        count += 1 
    print('\n')

