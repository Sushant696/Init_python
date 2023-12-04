# End and sep method in python 

# end
# print('Hello', end ="_")
# print("world") 
# output Hello_world 

# print('2020','10','12',sep='/')

a="$Capital"

print(a.center(10,"*"))

# python string formattinng using the templates class 
from string import Template

Template("$placeholder").substitute(placeholder="real value")

a = Template('hi i am $name and i am a $who.')
b = a.safe_substitute(name ='sushant', who = 'react developer')
print(b)

