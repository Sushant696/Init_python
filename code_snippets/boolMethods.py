# All the methods that returns value in bool

# string

# ___________________ Startswith ___________________

string = 'I love python programming'

# print(string.startswith('I love python'))

# ____________________ endswith________________________

# print(string.endswith('ing'))


# check if the string is alphabet , space , digit , number ans so on

# ____________________ isalnum ________________________


# print(string.isalnum()) # if only alphabet and number true else false for all event for space

#
# ____________________ isdigit _______________________

# string1 = '12' # only digits than true
# print(string1.isdigit())


# ____________________ isalpha ________________________
string2 = 'only alphabet no spaces or it will be false like this'
# print(string2.isalpha())

# ____________________ isnumeric ________________________
# print("12345".isnumeric())  # True
# print("hello123".isnumeric())

# ____________________ isprintable ________________________

# print('this is a printable , if only one non-printable is found  then the final result is false.\t '.isprintable()) # true can allow space and digit just check if there is printable or no if printable then it's true



# ____________________ isupper and islower ________________________

string1 = 'if only one lower or upper then both returns false they should be either 1 fully lower or fully upper'
# print(string1.islower())


# ____________________ find ________________________

string = 'found than index of that element if not found return -1'
# print(string.find('found')) search from beginning or left 

# ____________________ rfind ________________________

# print(string.rfind('found')) search from last or right

# istitle
# isinstance
# isdecimal

# string = 'is title check if the each work in string has capital first letter in each work if the first letter is not capital then it\'s not title'
# print('0100'.isdecimal())

# real and imag in python (complex numbers)

# complex is represent this way (a + bj) a is real part and b is imaginary part where j is the imaginary unit .
# complex_number =  4j
# _____________________ The real part can be zero but real can't be zero and if real is zero then you get 0.0 ___ you don't get error if you didn't write real part you still get 0.0
 
# print(complex_number.real , complex_number.imag) # 1.0 4.0


# a = [1,2,3,4,5,6]
# a.pop(a[3])
# print(a)

# a={1,2,3,4}
# a.add((2,3))
# print(a)


# start = 10
# end = 50

# for num in range(start, end + 1):
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 break
#         else:
#             print(num)


# string = "Hello world is  this is me sushant is babu prasai"
# print(string.split('me',4))
