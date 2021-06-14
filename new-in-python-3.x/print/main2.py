import sys


def main():
    if sys.version_info[0] < 3:
        # python2
        print (sys.version_info[0])

        # ('Hello', 'World!')
        print("Hello", "World!")

        # The answer is 4  -->  SyntaxError if use python3
        print "The answer is", 2*2

        # Trailing comma suppresses newline
        print "x",
        print "y"
        print "z"

        # Prints a newline
        print "Start a newline"
        print
        print "End a newline"

        # >> sys.stderr part makes the print statement output to stderr instead of stdout
        print >> sys.stderr, "fatal error"

        # ('x', 'y')
        x = 'x'
        y = 'y'
        print (x, y)

        # soft space
        print "A\n", "B"

if __name__ == "__main__":
    sys.exit(main())
