given_string = input('Enter a string')
first_char = given_string[0]
for i in range(1, len(given_string)):
    if given_string[i] == first_char:
        new_string = given_string[0:i] + '$' + given_string[i+1:]
        given_string = new_string
print(new_string)


