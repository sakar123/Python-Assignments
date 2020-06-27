"""23. Write a Python program to check a list is empty or not."""


def check_empty(a):
    if len(a) == 0:
        print("empty list!!")
    else:
        print("non-empty list!!")
    return ''


a = []
b = [1, 2, 3, 4]
print(check_empty(a))
print(check_empty(b))
