# basic function in python

# 3 types of function
# built in functions print() , upper() , input() , len()
# functions defined in modules ceil(), floor()
# user defined functions

# example of user defined functions

# def myfunc ():
#     return "hello returned by function"

# a = myfunc()
# print(a)

# functions with arguments

# def fun (name):
#    return f"my name is {name}"

# b = fun('sushant')
# print(b)


# positional arguments passing arguments in sequence

# def fun (b,a,c):
#    return a + b + c

# b = fun(20,10,30)
# print(b)


# keyword arguments

# def fun(a, b):
#     return a + b    

# b = fun(a=10, b=20)
# print(b)


# variable length arguments

# def fun(*a):
#     return a

# b = fun(10, 20,30,40)
# print(b)

# keyword variable length 

# def fun(**a):
#     return a

# b = fun(a= 10 , b = 20, c =30)
# print(b)

print('before def')
def sum (a):
    sum = 10
    for i in  a:
        sum += i
    return sum 

print('after def')
b = sum(a = [1,2,3,4])
print(b)
print('after call')