"""34. Write a Python script to merge two Python dictionaries."""


def merge_dicts(dict1, dict2):
    dict3 ={}
    for d in dict1, dict2:
        dict3.update(d)
    return dict3


print(merge_dicts({'Name': 'Sakar', 'Age': 22}, {'LastName': 'Poudel'}))
