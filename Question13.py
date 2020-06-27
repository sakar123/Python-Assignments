"""Write a Python program that accepts a comma separated sequence of words
as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red"""
given_words = input('Enter words separated with coma')
list_of_words = given_words.split(',',)
list_of_words.sort(key=str.lower)
print(list_of_words)

