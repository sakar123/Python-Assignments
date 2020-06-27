"""17. Write a Python program to multiplies all the items in a list."""
"""16. Write a Python program to sum all the items in a list."""
given_list = input('Enter numbers in the list')
given_list_string= given_list.split()
given_list_sum = []
mul = 1
for i in given_list_string:
    given_list_sum.append(int(given_list_string[given_list_string.index(i)]))
    mul = mul * given_list_sum[given_list_string.index(i)]
print("The product of given list is %s" % mul)