import sys


"""
filter creates a list of elements for which a function returns true
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        number_list = range(-5, 5)
        # number_list  range(-5, 5)
        print ("number_list ", number_list)

        less_than_zero = filter(lambda x: x < 0, number_list)

        print ("type(less_than_zero) ", type(less_than_zero))
        # less_than_zero  <filter object at 0x101c96cf8>
        print ("less_than_zero ", less_than_zero)
        # list(less_than_zero)  [-5, -4, -3, -2, -1]
        print ("list(less_than_zero) ", list(less_than_zero))

        # If function is None, the identity function is assumed, that is, all elements of iterable that are false are removed
        res = filter(None, number_list)

        print ("type(res) ", type(res))
        # res  <filter object at 0x101c96d30>
        print ("res ", res)
        # list(res)  [-5, -4, -3, -2, -1, 1, 2, 3, 4]
        print ("list(res) ", list(res))

        randomList = [1, 'a', 0, False, True, '0']
        filteredList = list(filter(None, randomList))
        # [1, 'a', True, '0']
        print (filteredList)

if __name__ == "__main__":
    sys.exit(main())
