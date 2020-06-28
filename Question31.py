"""31. Write a Python program to iterate over dictionaries using for loops."""

made_dictionary = {'Name': 'Sakar', 'Age': 22, 'Height': 5.9}

for i in made_dictionary:
    if i == 'Name':
        made_dictionary[i] = 'Changed'
    elif i == 'Age':
        made_dictionary[i] = 24
    elif i== 'Height':
        made_dictionary[i] = 6.0
    else:
        break
print(made_dictionary)

