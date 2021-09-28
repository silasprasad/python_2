# this works as follow
# factorial(4)
# 4 * factorial(3)
# 4 * 3 * factorial(2)
# 4 * 3 * 2 * factorial(1)
# 4 * 3 * 2 * (checks on if loop and returns 1)
# 4 * 3 * 2 * 1

def factorial(n):
    if n==0 or n==1:
        return n
    else:
       return n* factorial(n-1)
        #return n+ factorial(n-1) **Sum of n natural number
    

a = factorial(4)
print(a)