import sys


"""
dict methods dict.keys(), dict.items() and dict.values() return views instead of lists
"""


def main():
    dict_sample = {
        'a': 1,
        'b': [2, 3],
        'c': '4',
        'd': {'e': 5}
    }

    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        # k is  dict_keys(['a', 'b', 'c', 'd'])
        # k's type  <class 'dict_keys'>
        k = dict_sample.keys()
        print ("k is ", k)
        print ("k's type ", type(k))

        # i is  dict_items([('a', 1), ('b', [2, 3]), ('c', '4'), ('d', {'e': 5})])
        # i's type  <class 'dict_items'>
        i = dict_sample.items()
        print ("i is ", i)
        print ("i's type ", type(i))

        # v is  dict_values([1, [2, 3], '4', {'e': 5}])
        # v's type  <class 'dict_values'>
        v = dict_sample.values()
        print ("v is ", v)
        print ("v's type ", type(v))

        # the dict.iterkeys(), dict.iteritems() and dict.itervalues() methods are no longer supported
        #dki = dict_sample.iterkeys()
        #print (dki.next())
        #print (dki.next())

        # AttributeError: 'dict_keys' object has no attribute 'sort'
        # k.sort()
        print ("sorted(k) ", sorted(k))

if __name__ == "__main__":
    sys.exit(main())
