def factorial(n):
    if n==0 or n==1:
        return n
    else:
        return n* factorial(n-1)

a = factorial(5)
print(a)