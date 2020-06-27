"""21. Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]"""


def sorted_tuple(a):
    for i in range(0, len(a)-1):
        for j in range(0, len(a)-1):
            if a[j][1] > a[j+1][1]:
                swap = a[j+1]
                a[j+1] = a[j]
                a[j] = swap
                print(a, i)
    return a


print(sorted_tuple([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))



