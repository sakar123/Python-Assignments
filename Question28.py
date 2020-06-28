"""28. Write a Python script to add a key to a dictionary.

Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}"""

import sys


def add_key(given_dict, value, key):
    given_dict[key] = int(value)
    print(given_dict)


def main():
    if len(sys.argv) <= 2:
        print("not enough arguments provided")
    else:
        function = sys.argv[1]
        if function == "add_key":
            value = sys.argv[3]
            key = sys.argv[2]
            add_key({0: 10, 1: 20}, value, key)


if __name__ == '__main__':
    main()



