# reduce function 

# from functools import reduce

# numbers = [1,4,2,5,3,53,365,91]
# result = reduce(lambda x,y : x + y,numbers)
# print(result)

# set is a built-in data type in python which represent unordered collection of unique elements 

# myfirstset = {1,2,3,4,5,6,6,7,4}

# set1 = {1,2,4,53,2}
# set1.pop()
# # print(set1)



# a = {1,2,3,4,53,2}
# b = {94,63,62,731,62}
# u = a.union(b)
# d = a.difference(b)
# print(u,d)


# # is subset
# print(a.issubset(b))
# # is superset
# c = a.issuperset(b)
# print(c)



# dict
# mydict = {"key1" : 123 , 1 : 'abc'}
# # print(mydict[1])
# c = mydict.setdefault('c','cat') #returns the value if already in the dict than returns that value which is present in the dict
# # print(mydict)
# f = mydict.get('key1','key not avaliable')
# print(f)

# update the value
# mydict['key1'] = 7
# print(mydict)
# update the key 
a= {"a":2,"b":23}
oldKey= 'a'
newKey = 'Z'
a[newKey] = a.pop(oldKey)
print(a)

# some set methods are 
# myfirstset.add(8)
# myfirstset.remove(5)
# Add and remove can remove any element from anywhere 

# indexing is not supported in set

# can iterate over set 
# for i in myfirstset:
#     print(i)
# print(myfirstset)

# list 

# append add single value at last 
# extend add an iterable at last 
# insert can add at specific element

# pop default remove last element but can also remove specific element
# remove


# a = [1,2,3,4]
# a.remove


# a = [1,2,3,4,5]
# b= a.clear()
# print(a,b)

# a = (1,2,3,4)
# orglist = list(a)
# orglist.insert(2,'ram')
# # print(orglist)
# a = tuple(orglist)
# print(a)





