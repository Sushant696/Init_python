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


sum = lambda x , y: x + y
print(sum(2,3))

# doesn't 



