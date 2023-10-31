# python problems

# Write a Python script to add a key to a dictionary.
dict1 = {
    1: 'hello',
    2: 'namaste',
    3: 'bonjour',
}

# print(dict1)
# use can you the update method to replace a value too.
dict1.update({4: 'hi'})
# print(dict1)

# concatenate dictionaries with each other
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

dic4 = {**dic1, **dic2, **dic3}
# print(dic4)

# using chainMap method // should import from collections for the chainmap to work
# dict4 = chainmap(dic1,dic2,dic3)
# print(dict4)


# write a python script to check whether a given key already exist in a dictionary if it doesn't exist add the value with appropriate key


mydictionary = {
    "name": "sushant",
    'age': 18,
    "Totallevel": 100,
    "current_level": 17
}

if "id" in mydictionary:
    print("The key already exist")
else:
    mydictionary['id'] = 19
    # print(mydictionary)

# write a python program to iterate over dictionaries using for loop
dic = {
    '1': "1",
    2: 2*2,
    3: 3*3
}

# for key in dic:
#     print(key , "=",dic[key])


# Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
n = 15
dicts= {}
for i in range(1,n+1):
    dicts[i] = i * i
# print(dicts)

# write a python script to remove a item from dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop('model')
print((thisdict))

#  Write a Python program to multiply all the items in a dictionary.
