import sys


def main():
    dict_sample = {
        'a': 1,
        'b': [2, 3],
        'c': '4',
        'd': {'e': 5}
    }

    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

        # k is  ['a', 'c', 'b', 'd']
        # k's type  <type 'list'>
        k = dict_sample.keys()
        print "k is ", k
        print "k's type ", type(k)

        # i is  [('a', 1), ('c', '4'), ('b', [2, 3]), ('d', {'e': 5})]
        # i's type  <type 'list'>
        i = dict_sample.items()
        print "i is ", i
        print "i's type ", type(i)

        # v is  [1, '4', [2, 3], {'e': 5}]
        # v's type  <type 'list'>
        v = dict_sample.values()
        print "v is ", v
        print "v's type ", type(v)

        # Return an iterator over the dictionary's keys
        dki = dict_sample.iterkeys()
        print dki.next()
        print dki.next()

        k.sort()
        print "k.sort() ", k
        print "sorted(k) ", sorted(k)

if __name__ == "__main__":
    sys.exit(main())
