"""24. Write a Python program to clone or copy a list."""


def clone_list(given_list):
    new_list = []
    for i in given_list:
        new_list.append(i)
    return new_list


print(clone_list([1, 2, 3, 4, 5]))
print(clone_list([(1, 2), ('hello', 'ji')]))

