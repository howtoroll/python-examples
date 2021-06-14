import sys


"""
zip() now returns an iterator??
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        # no iterables are passed
        result = zip()
        # result:  <zip object at 0xxxxx>
        print ("result: ", result)

        x = [1, 2, 3]
        y = [4, 5, 6]

        zipped = zip(x, y)
        # type(zipped):  <class 'zip'>
        print ("type(zipped): ", type(zipped))
        # zipped:  <zip object at 0xxxxx>
        print ("zipped: ", zipped)
        # list(zipped):  [(1, 4), (2, 5), (3, 6)]
        print ("list(zipped): ", list(zipped))

        # different number of elements in iterables
        numbersList = [1, 2, 3]
        strList = ['one', 'two']
        numbersTuple = ('ONE', 'TWO', 'THREE', 'FOUR')
        result = zip(numbersList, strList, numbersTuple)
        # list(result):  [(1, 'one', 'ONE'), (2, 'two', 'TWO')]
        print ("list(result): ", list(result))

        # unzipping the value using zip()
        coordinate = ['x', 'y', 'z']
        value = [3, 4, 5, 0, 9]

        result = zip(coordinate, value)
        resultList = list(result)
        # [('x', 3), ('y', 4), ('z', 5)]
        print(resultList)

        c, v = zip(*resultList)
        # c:  ('x', 'y', 'z')
        print ('c: ', c)
        # v:  (3, 4, 5)
        print ('v: ', v)

if __name__ == "__main__":
    sys.exit(main())
