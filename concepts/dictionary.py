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
    "brand" : "Rolls Royace",
    "model" : "Ghost",
    "price" : "50cr",
    "price"  : "48cr"
}

# print(cars)

# The Dublicate keys are not allowed which means the second key will override the first key

# we can store any data type inside of dictionary even lists and tuple


# *** find length of dictionary ***
# print(len(cars))

bikes = {
    "brand" : "Kawashaki",
    "model" : "H2R",
    "top speed" : 342,
    "power" : "300BHP"
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
print(c)

# Check if key exits

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print(f"{thisdict['model']} exits in thisdict dictionary")
    