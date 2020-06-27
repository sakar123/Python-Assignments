given_string = input('Enter a string ')
given_index = int(input('which index do you want to remove? '))
string_to_return = given_string[:given_index] + given_string[given_index+1:]
print(string_to_return)