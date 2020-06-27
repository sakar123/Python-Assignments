"""18. Write a Python program to get the largest number from a list."""
given_list = input('Enter numbers in the list')
given_list_string= given_list.split()
given_list_sum = []
largest = int(given_list_string[0])
for i in given_list_string:
    given_list_sum.append(int(given_list_string[given_list_string.index(i)]))
    if given_list_sum[given_list_string.index(i)] > largest:
        largest = given_list_sum[given_list_string.index(i)]
print("The largest number of given list is %s" % largest)



