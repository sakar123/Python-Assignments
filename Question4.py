a = input('Enter the first string')
b = input('Enter the second string')
temp_a = a
temp_b = b
a = temp_b[0:2] + a[2:]
b = temp_a[0:2] + b[2:]
print(a, b)
