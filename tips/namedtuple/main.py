import sys
from collections import namedtuple


def profile():
    Person = namedtuple('Person', 'name age')
    return Person(name="Danny", age=31)


def main():
    # Use as namedtuple
    p = profile()
    print(p, type(p))  # Person(name='Danny', age=31) <class '__main__.Person'>
    print(p.name)
    print(p.age)

    # Use as plain tuple
    p = profile()
    print(p[0])
    print(p[1])

    # Unpack it immediatly
    name, age = profile()
    print(name)
    print(age)


if __name__ == "__main__":
    sys.exit(main())
