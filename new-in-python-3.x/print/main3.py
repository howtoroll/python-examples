import sys


"""
Print Is A Function
"""


def main():
    if sys.version_info[0] >= 3:
        # python3
        print (sys.version_info[0])

        # Hello World!
        print("Hello", "World!")

        # The answer is 4
        print("The answer is", 2*2)

        # Appends a space instead of a newline
        print("x", end=" ")
        print("y")
        print("z")

        # Prints a newline
        print("Start a newline")
        print()
        print("End a newline")

        # >> sys.stderr part makes the print statement output to stderr instead of stdout
        print("fatal error", file=sys.stderr)

        # ('x', 'y')
        x = 'x'
        y = 'y'
        print((x, y))

        # customize the separator
        print("There are <", 2**32, "> possibilities!", sep="")

        # no soft space
        print("A\n", "B")

if __name__ == "__main__":
    sys.exit(main())
