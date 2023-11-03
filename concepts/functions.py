# welcome to python functions
def my_func():
    {
        print('hello word')
    }

# what are arguments and parameters let's revise this concept


def new_function(param):
    {
        print(param)
    }


new_function('args passsed when function called and used inside the function as parameter \n parameter is just a copy of argument')

# if you don't know how many args are going to be passed into the function then you can do something like this :


def func(*param):
    {
        print('the first args', param[1])
    }


func('argument1', 'argument2', 'argument3')

# Note: here you will receive tuple of argument and to access 2nd or third parameter then you can use indexing like you use with tuple

# you can send args in the form of key value pairs

def fun(child1,child2):
    {
        print(child1)
    }
fun(child1='sushant',child2='someone')

# Note : while using this kind of arguments in your function than the parameter and the arguments name should be similar 