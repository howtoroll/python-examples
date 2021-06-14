import sys
import itertools


"""
map applies a function to all the items in an input_list
"""


def main():
    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

        items = [1, 2, 3, 4, 5]
        squared = []
        for i in items:
            squared.append(i**2)

        print "items ", items
        print "squared ", squared

        items = [1, 2, 3, 4, 5]
        res = map(lambda x: x**2, items)
        squared = list(res)

        print "items ", items
        print "type(res) ", type(res)
        print "res ", res
        print "squared ", squared

        def add_to_str(x, y):
            return str(x) + str(y)

        def f(*x):
            return x

        # In Python 2, a common (old, legacy) idiom is to use map to join iterators of uneven length using the form map(None,iter,iter,...) like so:
        for i in xrange(5):
            print i
        for i in xrange(10, 12):
            print i

        # ['010', '111', '2None', '3None', '4None']
        print map(add_to_str, xrange(5), xrange(10, 12))

        # [(0, 10), (1, 11), (2, None), (3, None), (4, None)]
        print map(None, xrange(5), xrange(10, 12))

        # [(0, 10), (1, 11), (2, None), (3, None), (4, None)]
        print map(f, *zip(*itertools.izip_longest(range(5), range(10, 12))))

        # [(10, 0), (11, 1), (None, 2), (None, 3), (None, 4)]
        print map(None, xrange(10, 12), xrange(5))

if __name__ == "__main__":
    sys.exit(main())
