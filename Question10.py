"""Write a Python program to remove the characters which have odd index
values of a given string."""

given_string = input('Enter a string')
to_return = given_string.split()
for i in to_return:
    if to_return.index(i) % 2 != 0:
        to_return.pop(to_return.index(i))
to_return_string = ' '
print(to_return_string.join(to_return))
