# will do some string stuff 
# what is string in python??

normalString = "hello world this i am a normal string"
multilineString = """hello this is 
multiline string
right here!!"""
# print(multilineString)
# print(multilineString[1]) 


# loop through array 
list1 = []
for i in normalString :
    list1.append(i)

# print(list1)

string = 'my name is sushant babu prasai.'
# check if babu is present in the string using in operator 
# print('babu' in string)

# slicing in strings 
string = 'sushant babu prasai'
myname = string[0:7]
# print(myname)

# negative indexing in python 
myStr = 'hello babe'
# print(myStr[:5:-1]) 

# Let me show you the working mechanism of the slicing in python 

mystr1 = 'happy slicing'
start = 0 
stop = len(mystr1)
step = -2 # to travel backward use -1 
print(mystr1[start:stop:step],'hello is it working?')

