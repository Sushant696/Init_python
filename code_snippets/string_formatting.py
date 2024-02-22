# formatting using %  operator

string = "hello"


# # number of place holders == number of values provided

string1 = '%s world' % string
print(string1)


# format method for formatting

string = 'python'
string1  = "programming"

result = 'i love {0} {0}'.format({string})
# names arguments
result = 'i love {greeting} {age}'.format(greeting  = string , age = 'string1' )

# positional arguments
result = 'i love {0} {1}'.format(string , string1 )
print(result)


# # cannot use manual with automatic field numbering

# result = 'i love {} {1}'.format(string , string1 ) #error
# print(result)


# make trans and translate

string = 'hello'
translation_table = string.maketrans("hello", "olleh")
print(translation_table)

translated_string = string.translate(translation_table)
print(translated_string)


# so there is the string which content we want to replace right 
# make trans method translate the thing by translating each character on the basis of ascii table
# make trans method returns dictionary with indiviual ascii value changed first character or key  to be the orginal string character and the second or value to be the value to be changed ascii value

# The translate method takes in the data or ascii value as in the form of dictionary and changes it.
 

print("Welcome {} softwarica".format("tw")) 