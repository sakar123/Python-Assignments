""" 32. Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}"""


def square_upto(n):
    dictionary ={}
    for i in range(1, n+1):
        dictionary[i] = i*i
    return dictionary


print(square_upto(5))