"""16. Write a Python program to sum all the items in a list."""
given_list = input('Enter numbers in the list')
given_list_string= given_list.split()
given_list_sum=[]
for i  in given_list_string:
    given_list_sum.append(int(given_list_string[given_list_string.index(i)]))
sum_of_list = sum(given_list_sum)
print("The sum of given list is %s" % sum_of_list)