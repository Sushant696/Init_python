# # what is scope and concept of scope in python

# x = 4
# print("global x",x)

# def  hello():
#     global x
#     x = 2
#     print('local  x',x)

# hello()
# print('global x' , x)

# the scoping is pretty simple in python there are just local and global scope,

# Local variables means variable that are defined inside function and aren't accessible outside that function
# Global variables means variable that defined outside any particular function and is accessible to any function

# if you want to use an local  variable outside function or want to use the global variable inside function and manipulate it's value than you can use the global keyword


# sum = lambda x , y: x + y
# print(sum(2,3))

# doesn't


# name space
# namespace is a system to control names in python program. it ensures names are unique and there are no conflicts in names

# local namespace : covers local names inside of the function
# global namespace : covers global names imported from modules
# buildin namespace : covers build functions and build in exception names


# legb rule
# local scope : contains names inside of the functions
# global scope : Contains Names defined at the top level of the script or module.
# enclosed : scope between inner and outer function
# buildin : contains build-it names


# globalVar = 10
# def outer():
#     localVar = 12
#     globalVar = 15
#     print("lexical environment of inner")
#     def inner ():
#         print('inside of inner function')
#     inner()

# print("first one to execute")
# print(outer())

# def fun():
#     return 'hello world'
# print(fun())


# from math import *


# def add(a):
#     def inner(sum):
#         return sum + 1
#     sum = 0
#     for i in a:
#         sum = sum + i
#     return inner(sum)

# print(add([1, 2, 3, 4]))


# pi = 10 
# def add ():
#     pi = 21
#     def inner():
#         pi = 90
#         print(pi)
#     inner()
# b = add()
# print(b)


# import for turtle
import turtle

# Starting a Working Screen
ws = turtle.Screen()

# initializing a turtle instance
geekyTurtle = turtle.Turtle()

# executing loop 5 times for a star
for i in range(5):

		# moving turtle 100 units forward
		geekyTurtle.forward(100)

		# rotating turtle 144 degree right
		geekyTurtle.right(144)



