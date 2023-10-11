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
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in range(3): 
    for y in fruits:
        print(x,y)
    

# the inner loop will be executed one time for each iteration of the outer loop 
# pass statement does nothing but you can use pass to avoid getting error due to empty loops or conditionals



