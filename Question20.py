"""20. Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list of
strings.
Sample List : ['abc', 'xyz', 'aba', '1221']"""
given_strings = input('Enter the list pf strings')
made_list = given_strings.split()
count = 0
for i in made_list:
    if made_list[made_list.index(i)][0] == made_list[made_list.index(i)][-1]:
        count= count+1
print(count)