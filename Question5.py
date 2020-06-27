given_string = input('Enter a string')
if len(given_string) < 3:
    new_string = 'not a valid string'
else:
    if given_string[-3:] == "ing":
        new_string = given_string + 'ly'
    else:
        new_string = given_string + 'ing'
print(new_string)
