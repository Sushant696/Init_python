# there are 3 logical opertors
# And , or , not -- you use these keyword as logical operator not  && || these symbols in python 

x = 23 
y = 12
if x > y or x==y  :
    print("Either x is greater than y or they are equall") 
print(bool(not y))

# chaining comparision operator in python
grade = 90
if grade >= 90 and grade < 100:
    print("outstanding (A+)")
# by using the chaining comparision operator you can write this as 
if 90 <= grade < 100 :
    print("outstanding(A+)")   

# The results is same in both cases



# check if any string are empty or not using conditional statement 

name = '' #' ' if single space is in string then also the string is not considered as empty string 
if not name:
    print("The string is empty")
else :
    print("The string is not empty")