import sys


"""
PEP 237: Essentially, long renamed to int. That is, there is only one built-in integral type, named int; but it behaves mostly like the old long type.
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        # <class 'int'>
        print (type(65535))
        # <class 'int'>
        print (type(65536 * 65536))
        # <class 'int'>
        print (type(65536 * 65536 * 65536 * 65536))

if __name__ == "__main__":
    sys.exit(main())
