# what is string formatting ?
# string formatting in python is the process of inserting a custom string or variable in predefined text or existing text.
from string import Template

string = "String formatting.."

# Formatting string using the % operator
first_name = "sushant"
last_name = "prasai"
string = "Hi!, %s" % first_name
# print(string)

name = "jhon"
age = 34
profession = 'Software Engineer'
works_for = 'Google'

string = "my name is %s i am a %s at %s" % (name, profession, works_for)
string = "Inserted number is %5.2f" % 3.28364
print(string)

# print(string)
# If there are more than one strings that you want to insert in a string than use this tuple format.


# string formatting using string format() method
book_name = "Unthered Soul"
author = "Michael Alan Singer"

# can access the data using indexing too
new_string = 'My Favourite Book is  {0} it\'s written by {1}'.format(
    book_name, author)

# print(new_string)

# string formating using f string

emp_name = "Aron"
age = 23
degree = 'cs degree'
string = f"Emp name :{emp_name} Emp age {age} Emp Qualification : {degree.capitalize()}"
# print(string)

# MultiLine f string
std_name = "nissan"
age = 18
details = f"Student name is {std_name}"\
    f'student is {age} years old'
print(details)

# python string templates
s = Template("$who wants $what")
print(s.substitute(who='sushant' , what="Enthusiasm"))
print(s.safe_substitute(who='sushant' , what="Enthusiasm"))



# python center method for formatting

txt = 'banana'
ntxt = txt.center(20)
print(ntxt)
print(dir(txt))


