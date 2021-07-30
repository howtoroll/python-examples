import sys


def main():
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for key, value in enumerate(my_list):
        print(key, value)

    # specify the starting index of the counter
    my_list = ['apple', 'banana', 'grapes', 'pear']
    for key, value in enumerate(my_list, 1):
        print(key, value)


if __name__ == "__main__":
    sys.exit(main())
