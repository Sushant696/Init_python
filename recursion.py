
# # direct recursion 

def factorial(n):
    if n == 0 or n == 1:
        return 1  # base case
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)  # result = 120




# indirect recursion 

def even_number(n):
    if n == 0:
        return True
    else:
        return odd_number(n - 1)

def odd_number(n):
    return not even_number(n)

result = odd_number(6)
print(result)


