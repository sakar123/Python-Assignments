"""40. Write a Python program to add an item in a tuple."""


def add_to_tuple(given_tuple, to_add):
    new_tuple = ()
    new_tuple = given_tuple + to_add
    return new_tuple


print(add_to_tuple((1, 2, 3), (4,)))

# example of how i need to add a comma to a single item in a tuple to declare it as a tuple, else its declared as a
# string