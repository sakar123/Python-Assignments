"""19. Write a Python program to get the smallest number from a list."""
given_list = input('Enter numbers in the list')
given_list_string= given_list.split()
given_list_sum = []
smallest = int(given_list_string[0])
for i in given_list_string:
    given_list_sum.append(int(given_list_string[given_list_string.index(i)]))
    if given_list_sum[given_list_string.index(i)] < smallest:
        smallest = given_list_sum[given_list_string.index(i)]
print("The largest number of given list is %s" % smallest)
