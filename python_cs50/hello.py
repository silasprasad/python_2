# # Ask use input
# name = input('whats your name? ').strip().title()

# # Remove whitespace from str and capitalize
# # name = name.strip().title()

# # Say hello to users by passing input name
# print(f'hello, {name}')

def hello(to):
    print('hello,', to)

name = input('whats your name? ')
hello(name)