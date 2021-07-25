import sys


def add_to_v1(num, target=[]):
    target.append(num)
    return target


def add_to_v2(element, target=None):
    if target is None:
        target = []
    target.append(element)
    return target


def main():
    # mutable
    foo = ['hi']
    print(foo)

    bar = foo
    bar += ['bye']
    print(foo)  # The new variable is just an alias for the old variable. 

    print(add_to_v1(1))
    print(add_to_v1(2))
    print(add_to_v1(3))  # unexpected

    print(add_to_v2(1))
    print(add_to_v2(2))
    print(add_to_v2(3))  # expected


if __name__ == "__main__":
    sys.exit(main())
