import sys
import concurrent.futures


FIBS = [28, 10, 20, 20, 23]


def fib(n):
    if n < 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def main():
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for number, fib_value in zip(FIBS, executor.map(fib, FIBS)):
            print str(number) + " fib number is " + str(fib_value)


if __name__ == "__main__":
    sys.exit(main())
