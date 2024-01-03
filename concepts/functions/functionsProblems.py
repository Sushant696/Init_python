# def softwarica(a):
#     for i in range(1,11) :
#         print(i,a)

# softwarica("softwarica")

# print('before def')
# def sum (a):
#     sum = 10
#     for i in  a:
#         sum += i
#     return sum

# print('after def')
# b = sum(a = [1,2,3,4])
# print(b)
# print('after call')


#  print each character using indexing


# def fun(a):
#     for i in range(len(a)):
#         print(a[i])
# fun('softwarica')


# write a program to display integer from of a list. given list=[1,"a","c",2,3,4]
# mylist = [1,"a","c",2,3,4]

# def sum(lists):
#     for i in lists:
#         if (isinstance(i,int)):
#             print(f"{i} is integer")

# sum (mylist)

# multiplication of a each element. given

# def fun(lst):
#     for i in lst:
#         for j in range(1,11):
#             print(f"{i}*{j}={i*j}")


# my_list=[4,5,3,2]
# fun(my_list)


# multiplication table of a given number
def fun(num):
    for i in range(1, 11):
        print(f"{num}*{i}={num*i}")


user = int(input('Enter number to calculate it multiplication table'))
fun(user)