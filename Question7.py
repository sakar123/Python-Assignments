def longest(list_of_words):
    greatest = list_of_words[0]
    for i in list_of_words:
        if len(i) > len(greatest):
            greatest = list_of_words[list_of_words.index(i)]
    print(greatest)

given_strings = input('Enter list of strings separated with whitespaces')
obtained_list = given_strings.split()
longest(obtained_list)