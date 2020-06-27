"""15. Write a Python function to insert a string in the middle of a string.
Sample function and result :
insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}"""


def insert_string_middle(in_string, middle_string):
    to_return = in_string[:2] + middle_string + in_string [2:]
    return to_return


print(insert_string_middle('[[]]','Python'))



