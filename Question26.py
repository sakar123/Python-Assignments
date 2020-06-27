"""26. Write a Python program to insert a given string at the beginning of all items in
a list.

Sample list : [1,2,3,4], string : emp
Expected output : ['emp1', 'emp2', 'emp3', 'emp4']"""


def add_string_to_list(given_string, given_list):
    for i in given_list:
        given_list[given_list.index(i)] = given_string + str(i)
    return given_list


print(add_string_to_list('emp', [1, 1, 3, 4, 1]))



