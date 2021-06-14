import sys
from functools import cmp_to_key


"""
The ordering comparison operators (<, <=, >=, >) raise a TypeError exception when the operands don’t have a meaningful natural ordering
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

    try:
        print (1 < '')
    except TypeError as e:
        print ("1 < '': ", e)

    try:
        print (0 > None)
    except TypeError as e:
        print ("0 > None: ", e)

    try:
        print (None < None)
    except TypeError as e:
        print ("None < None: ", e)

    # does not apply to the == and != operators
    # True
    print (None == None)

    # False
    print (None != None)

    def reverse_numeric(x, y):  # reverse the order
        return y - x

    # In Py3.0, the cmp parameter was removed entirely

    # To convert to a key function, just wrap the old comparison function:
    # [5, 4, 3, 2, 1]
    print (sorted([5, 2, 4, 1, 3], key=cmp_to_key(reverse_numeric)))

    t_list = [5, 2, 4, 1, 3]
    t_list.sort(key=cmp_to_key(reverse_numeric))
    # [5, 4, 3, 2, 1]
    print (t_list)

if __name__ == "__main__":
    sys.exit(main())
