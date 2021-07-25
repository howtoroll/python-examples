import sys


def main():
    is_nice = True
    state = "nice" if is_nice else "not nice"
    print(state)

    print(True or "Some")
    print(False or "Some")

    output = None
    msg = output or "No data returned"
    print(msg)


if __name__ == "__main__":
    sys.exit(main())
