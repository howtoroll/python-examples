import sys


def calculate_fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


def main():
    # calculate_fibon(10) is a iterator
    for x in calculate_fibon(10):
        print(x)

    total = sum(calculate_fibon(10))
    print(total)


if __name__ == "__main__":
    sys.exit(main())
