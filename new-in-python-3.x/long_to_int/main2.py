import sys


def main():
    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

        # <type 'int'>
        print type(65535)
        # <type 'int'>
        print type(65536 * 65536)
        # <type 'long'>
        print type(65536 * 65536 * 65536 * 65536)


if __name__ == "__main__":
    sys.exit(main())
