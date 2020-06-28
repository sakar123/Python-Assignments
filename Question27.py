"""27. Write a Python program to replace the last element in a list with another list.
Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]"""


def replace(list_a, list_b):
    list_a.pop(-1)
    return list_a + list_b


print(replace([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]))

# another way to do the same problem

list_a = [1, 3, 5, 7, 9, 10]
list_b = [2, 4, 6, 8]
list_a[-1:] = list_b
print(list_a)
