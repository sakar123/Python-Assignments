"""25. Write a Python program to check whether all dictionaries in a list are empty or
not.

Sample list : [{},{},{}]
Return value : True

Sample list : [{1,2},{},{}]
Return value : False"""


def check_the_list(list1):
    if all(not d for d in list1) is True:
        print("Empty List")
    if all(not d for d in list1) is False:
        print("Not an empty list")


check_the_list([{},{},{}])
check_the_list([{1,2},{},{}])



