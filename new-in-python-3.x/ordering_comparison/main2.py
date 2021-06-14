import sys


def main():
    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

    # True
    try:
        print 1 < ''
    except TypeError:
        print "should not happen"

    # False
    try:
        print 1 > ''
    except TypeError:
        print "should not happen"

    # True
    try:
        print 0 > None
    except TypeError:
        print "should not happen"

    # False
    try:
        print None < None
    except TypeError:
        print "should not happen"

    # True
    print None == None

    # False
    print None != None

    def reverse_numeric(x, y):  # reverse the order
        return y - x

    # cmp function should take two arguments to be compared and then return a negative value for less-than, return zero if they are equal, or return a positive value for greater-than
    # [5, 4, 3, 2, 1]
    print sorted([5, 2, 4, 1, 3], cmp=reverse_numeric)

    t_list = [5, 2, 4, 1, 3]
    t_list.sort(reverse_numeric)
    # [5, 4, 3, 2, 1]
    print t_list

if __name__ == "__main__":
    sys.exit(main())
