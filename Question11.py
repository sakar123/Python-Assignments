"""Write a Python program to count the occurrences of each word in a given
sentence."""
given_sentence = input('Enter a sentence')
list_of_words = given_sentence.split()
to_return = {}
count = 1
for i in list_of_words:
    if i in to_return:
        to_return[i] = to_return[i] + 1
        continue
    else:
        to_return[i] = 1
print(to_return)
