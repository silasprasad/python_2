# i = 0

# while i < 3:
#     print("Meow")
#     i += 1


# for i in range(3):
#     print("Meow")

# using print func 

# print("Meow\n" * 3, end="")

""" using functions """

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("Meow")

main()