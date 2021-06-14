import sys
import itertools


"""
map applies a function to all the items in an input_list
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        items = [1, 2, 3, 4, 5]
        squared = []
        for i in items:
            squared.append(i**2)

        print ("items ", items)
        print ("squared ", squared)

        items = [1, 2, 3, 4, 5]
        res = map(lambda x: x**2, items)
        squared = list(res)

        print ("items ", items)
        print ("type(res) ", type(res))
        print ("res ", res)
        print ("squared ", squared)

        def add_to_str(x, y):
            return str(x) + str(y)

        def f(*x):
            return x

        for i in range(5):
            print (i)
        for i in range(10, 12):
            print (i)

        # <map object at xxx
        print (map(add_to_str, range(5), range(10, 12)))
        # ['010', '111']
        print (list(map(add_to_str, range(5), range(10, 12))))

        # <map object at xxx
        print (map(None, range(5), range(10, 12)))

        # 'NoneType' object is not callable
        #print (list(map(None, range(5), range(10, 12))))
        # [(0, 10), (1, 11)]
        print (list(map(f, range(5), range(10, 12))))

        # [(0, 10), (1, 11), (2, None), (3, None), (4, None)]
        print (list(map(f, *zip(*itertools.zip_longest(range(5), range(10, 12))))))

        # <map object at xxx
        print (map(None, range(10, 12), range(5)))

        # 'NoneType' object is not callable
        #print (list(map(None, range(10, 12), range(5))))
        # [(10, 0), (11, 1)]
        print (list(map(f, range(10, 12), range(5))))

if __name__ == "__main__":
    sys.exit(main())
