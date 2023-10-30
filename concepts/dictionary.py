# Dictionary are like objects of javascript the data are stored in key value pairs in dictionary..abs

# my_first_dict = {
#     "name" : 'sushant babu prasai',
#     "roll ": 23 ,
# }

# print(my_first_dict)

# cars = {
#     "brand" : "Rolls Royace",
#     "model" : "Ghost",
#     "price in NPR" : "50cr"
# }
# Access individual data from  dictionary using it's key

# ** Dictionary are mutable meaning that we can manipulate dictionary after it has been created **

cars = {
    "brand": "Rolls Royace",
    "model": "Ghost",
    "price": "50cr",
    "price": "48cr"
}

# print(cars)

# The Dublicate keys are not allowed which means the second key will override the first key

# we can store any data type inside of dictionary even lists and tuple


# *** find length of dictionary ***
# print(len(cars))

bikes = {
    "brand": "Kawashaki",
    "model": "H2R",
    "top speed": 342,
    "power": "300BHP"
}
# print(type(bikes))
a = bikes['brand']
# print(a)

x = bikes.keys()
# print(x)

# Changing values from the

bikes['model'] = "Zx 10r"
# print(bikes['model'])

# Get the list of all the values of the dictionary
b = bikes.values()
# print(b)

# Get each items of dictionary, as tuples in list
c = bikes.items()
# print(c)

# Check if key exits

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# if "model" in thisdict:
#     print(f"{thisdict['model']} exits in thisdict dictionary")


newdict = {
    'name': "sushant babu prasai",
    'profession': "Enterpreneur",
    'networth': '10 Billion',
}

# adding new item to the dictionary
# print(newdict)

newdict['id'] = 101
# print(newdict)

# Get all the values of the dictionary

a = newdict.values()
# print(a)

# using list as value inside of dictionary

list_dict = {
    'mylist': ['hello', 'i', 'am', 'a', 'list'],
    'tuple': ('hello i am tuple'),
    "number": 777,
    'bool': True
}

# inner_list = list_dict["mylist"]
# string = ''
# for i in inner_list:
#     string += ' ' + i
# print(string)


# using alternative methods
inner_list = list_dict["mylist"]
string = ' '.join(inner_list)
# print(string)

# you can even set the key as list or tuple
dict2 = { 
    "name" : 'sushant',
    'age'  : 18,
    'status' : 'focused',
    ('me','myself') : 'i'   
}

# print(dict2.items())

# update dictionary using update method
dict1 = {
    'name' : 'python',
    'age'  :  22 ,
    'founder' : "Guido van rossum"
    }
dict1.update({'year' : 1991})
# print(dict1)


# Remove item from dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'category' : 'car'
}
thisdict.pop('year')
thisdict.popitem() # removes the last element of the dictionary

# delete item with specific keyword
del thisdict['brand']

# delete the whole dictionary
thisdict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  'category' : 'car'
}
# del thisdict1 
# print(thisdict1) (will cause error as the thidict1 don't exist)


# make the dictionary empty
thisdict1.clear()
print(thisdict1)