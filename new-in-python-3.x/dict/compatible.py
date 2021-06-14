import sys
import six


def main():
    dict_sample = {
        'a': 1,
        'b': [2, 3],
        'c': '4',
        'd': {'e': 5}
    }

    # python2 or python3
    six.print_(sys.version_info[0])

    # k is  ['a', 'c', 'b', 'd']
    k = dict_sample.keys()
    six.print_("k is ", k)
    six.print_("k's type ", type(k))

    # i is  [('a', 1), ('c', '4'), ('b', [2, 3]), ('d', {'e': 5})]
    i = dict_sample.items()
    six.print_("i is ", i)
    six.print_("i's type ", type(i))

    # v is  [1, '4', [2, 3], {'e': 5}]
    v = dict_sample.values()
    six.print_("v is ", v)
    six.print_("v's type ", type(v))

    # Return an iterator over the dictionary's keys
    dki = six.iterkeys(dict_sample)
    six.print_(six.next(dki))
    six.print_(six.next(dki))
    six.print_(six.next(dki))
    six.print_(six.next(dki))

    #k.sort()
    #six.print_("k.sort() ", k)
    six.print_("sorted(k) ", sorted(k))

if __name__ == "__main__":
    sys.exit(main())
