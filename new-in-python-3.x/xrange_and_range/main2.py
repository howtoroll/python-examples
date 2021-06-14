import sys


def main():
    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

        print "xrange(3)"
        for i in xrange(3):
            print i

        print "range(3)"
        for i in range(3):
            print i

        # with odd numbers
        print "xrange(1, 10, 2)"
        for i in xrange(1, 10, 2):
            print i

        print "range(1, 10, 2)"
        for i in range(1, 10, 2):
            print i

if __name__ == "__main__":
    sys.exit(main())
