"""Write a Python function to create the HTML string with tags around the
word(s).
Sample function and result :

add_tags('i', 'Python') -> '<i>Python</i>'
add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'"""

import sys

def create_html(tag, given_words):

    print("<%s>%s</%s>" % (tag, given_words, tag))

def main():
    if len(sys.argv) <=2:
        print('not enough args')
    else:
        function = sys.argv[1]
        if function == "create_html":
            create_html(sys.argv[2], sys.argv[3])


if __name__ == '__main__':
     main()







