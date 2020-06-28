"""38. Write a Python program to remove a key from a dictionary."""

def remove_key(dict1, the_key):
    try:
        dict1.pop(the_key)
        return dict1
    except KeyError:
        print("Key not Found!!!")


print(remove_key({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}, 15))
