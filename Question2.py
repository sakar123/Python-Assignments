string_given = input('Enter a string please')
if len(string_given) == 1:
    to_return = 'Empty String'
elif len(string_given) < 3:
    to_return = string_given * 2
else:
    to_return = string_given[0:2] + string_given[-2:]
print(to_return)
