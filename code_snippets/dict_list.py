# # append 

# # add items to end of the list
# # mylist  = [1,2,3,4,5]
# # mylist.append(11)
# # print(mylist)

# # Insert

# # insert(index , element)
# # mylist.insert(1,'second')
# # print(mylist)

# # Extend iterable at the end 
# mylist = [1,2,3,4]
# # extended_items = [2,3,45]
# # mylist.extend(extended_items)
# # print(mylist)

# # copy 
# # copied_items = mylist.copy()
# # print(copied_items) 


# # count method
# # print(copied_items.count(405)) # search for specified items and return number of occurences

# # index
# # print(mylist.index(4))

# # _______________ pop 
# # a= mylist.pop(2)
# # print(a)


# # _________________ remove

# # mylist = [1,2,3,5,32,62,53]
# # print(mylist.remove(3) , mylist) 


# ___________________ reverse
mylist = [1,2,3,5,32,62,53]
reversed_list = mylist.reverse()
# print(mylist)


# # ____________________sort

# mylist = [1,2,3,5,32,62,53]
# print(mylist.sort(reverse=True) , mylist)



# # Use remove() when you want to remove the first occurrence of a specific element.

# # Use pop() when you need to remove an element at a specific index or the last element (default).



# dictionary in python 

dic = {1 : "value" , 2 : 'value 2'}

# method for dictionary
# a= dic.keys() # returns view of  keys
# b = dic.values() # returns view of  values
# print(a,b)

a = dic.items() #key value pairs as tuple dict_items{(key : value), (key : value)}


my_dict = {1 : "value" , 2 : 'value 2'}
value = my_dict.get("age")
# print(value)  # Output: 30

value = my_dict.get("city", "Unknown")
# print(value)  # Output: Unknown

# pop and popitems 
# pop removes specific key value pairs

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# popped_value = my_dict.pop('b')
# print(popped_value)  # Returns removed items valu e
# print(my_dict)       # Output: {'a': 1, 'c': 3}


# pop item
my_dict = {'a': 1, 'b': 2, 'c': 3}
popped_value = my_dict.popitem()
# print(popped_value)  
# print(my_dict) 

# updating dictionary with adding or merging another dictionary
# other_dict = {"city": "New York" , "a" : 2}
# my_dict.update(other_dict)
# print(my_dict)  

# when merging if any pair have same key the existing key will be over ridden!!!


# my_dict = {'a': 1, 'b': 2, 'c': 3}
# a = my_dict.get('d')
# print(a)


# lambda function
# a , b = 7 , 4
# abc = lambda a ,b : a + b
# print(abc (a= 3 , b = 5))


S = {'red', 'green', 'blue'}
S.add('yellow')
print(S)