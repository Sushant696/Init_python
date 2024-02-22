# set copy method
# set1 = {1, 2, 3, 4}
# copied_set = set1.copy()
# copied_set.add((1, 2))
# print(copied_set)


# ------------------ remove method ---------------
# a = set1.remove() # returns none throw an error
# print(set1.discard(0)) # retuns none do not throw error
# print(set1) 

# Intersection

sets = {1,6,2,4}
sets1 = {2,4,22,5}
newset = sets.intersection(sets1)
# print(newset,sets1,newset)


# returns element not in both sets
# symmetric__difference = sets ^ sets1
# print(symmetric__difference)

# subset and super set
# set1 = {1,2,3,4,5}
# set2 = {1,2,3,4,5,19,23,6}

# superset = set2.issuperset(set1)
# subset = set1.issubset(set2)
# print(superset,subset)