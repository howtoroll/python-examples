import sys


# __slots__ : tell Python not to use a dict to store an object’s instance attributes, and only allocate space for a fixed set of attributes.
class MyClass:
    __slots__ = ['name', 'identifier']

    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.set_up()


def main():
    pass


if __name__ == "__main__":
    sys.exit(main())
