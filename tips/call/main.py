import sys


class Example:
    def __init__(self, x):
        print('x in __init__', x)

    def __new__(cls, y):
        print('y in __new__', y)
        return super(Example, cls).__new__(cls)

    def __call__(self, z):
        print('z in __call__', z)


class RegexValidator:
    def __call__(self, value):
        print('RegexValidator logic')


class URLValidator(RegexValidator):
    def __call__(self, value):
        super(URLValidator, self).__call__(value)
        print('URLValidator logic')


class EmailValidator(RegexValidator):
    def __call__(self, value):
        super(EmailValidator, self).__call__(value)
        print('EmailValidator logic')


def main():
    # x is an instance
    # x(arg1, arg2, ...) is a shorthand for x.__call__(arg1, arg2, ...)
    Example('123')('abc')

    # same interface
    for v in [URLValidator(), EmailValidator()]:
        v('test')


if __name__ == "__main__":
    sys.exit(main())
