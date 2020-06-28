"""30. Write a Python script to check whether a given key already exists in a
dictionary."""


def check_key(given_dict, key):
    if key in given_dict:
        print("Key already exists!!!")
    else:
        print("Key does not exist!!!")


check_key({'1': 10, 2: 20}, 3)
