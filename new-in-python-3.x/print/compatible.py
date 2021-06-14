import sys
import six


def main():
    # python2 or python3
    six.print_(sys.version_info[0])

    # Hello World!
    six.print_("Hello", "World!")

    # The answer is 4
    six.print_("The answer is", 2*2)

    # Appends a space instead of a newline
    six.print_("x", end=" ")
    six.print_("y")
    six.print_("z")

    # Prints a newline
    six.print_("Start a newline")
    six.print_()
    six.print_("End a newline")

    # >> sys.stderr part makes the print statement output to stderr instead of stdout
    six.print_("fatal error", file=sys.stderr)

    # ('x', 'y')
    x = 'x'
    y = 'y'
    six.print_((x, y))

    # customize the separator
    six.print_("There are <", 2**32, "> possibilities!", sep="")

    six.print_()

    # no soft space
    six.print_("A\n", "B")

if __name__ == "__main__":
    sys.exit(main())
