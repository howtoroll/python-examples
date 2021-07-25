import sys


def main():
    # Intersection
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown', 'black'])
    result = input_set.intersection(valid)
    print(type(result))  # <class 'set'>
    print(result)  # {'black', 'red'}


    # Difference
    valid = set(['yellow', 'red', 'blue', 'green', 'black'])
    input_set = set(['red', 'brown'])
    result = input_set.difference(valid)
    print(result)  # {'brown'}
    result = valid.difference(input_set)
    print(result)  # {'green', 'blue', 'black', 'yellow'}

    # old notation
    input_set = set(['red', 'brown'])
    print(type(input_set))
    # new notation
    input_set = {'red', 'brown'}
    print(type(input_set))


if __name__ == "__main__":
    sys.exit(main())
