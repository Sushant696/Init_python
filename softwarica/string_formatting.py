# what is string formatting ? 
# string formatting in python is the process of inserting a custom string or variable in predefined text or existing text.

string = "String formatting.."

# Formatting string using the % operator
first_name = "sushant"
last_name = "prasai"
string = "Hi!, %s" %first_name
# print(string)

name = "jhon"
age = 34
profession = 'Software Engineer'
works_for = 'Google'

string = "my name is %s i am a %s at %s" %(name ,profession , works_for) 
# print(string)
# If there are more than one strings that you want to insert in a string than use this tuple format.


# string formatting using string format() method   
book_name = "Unthered Soul"
author = "Michael Alan Singer"

new_string = 'My Favourite Book is  {} it\'s written by {}'.format(book_name,author)
print(new_string)

# string formating using f string

emp_name = "Aron"
age = 23
string = f"Emp name :{emp_name} Emp age {age}"
print(string)