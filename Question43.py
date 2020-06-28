"""43. Write a Python program to remove an item from a tuple."""

tuple_a = (1, 2, 3, 4, 5)
new_tuple = tuple_a[:-1]
tuple_a = new_tuple
print(tuple_a)