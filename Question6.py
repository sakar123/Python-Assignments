whole_string = input('Enter a complete sentence: ')
# continue until you find the not in the string
index_of_not = whole_string.find('not')
index_of_poor = whole_string.find('poor')

if index_of_poor > index_of_not > 0:
    to_return = whole_string[:index_of_not] + 'good' + whole_string[index_of_poor+4:]
else:
    to_return = whole_string
print(to_return)