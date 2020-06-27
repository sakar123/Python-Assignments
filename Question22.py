"""Write a Python program to remove duplicates from a list."""


def rem_dup_list(a):
    new_list = []
    for i in a:
        if i not in new_list:
            new_list.append(i)
    return new_list


print(rem_dup_list([1,1,2,3,4,5]))

