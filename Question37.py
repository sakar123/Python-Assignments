"""37. Write a Python program to multiply all the items in a dictionary."""


def prod_dicts(dict1):
    list_of_values = dict1.values()
    product_of_values = 1
    for i in list_of_values:
        product_of_values = i * product_of_values
    return product_of_values


print(prod_dicts({1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}))



