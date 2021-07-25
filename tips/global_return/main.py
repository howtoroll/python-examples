import sys

#Don’t use global keyword unless you know what you are doing.
# Global & Return
def add_a(value1, value2):
    result_a = value1 + value2


def add_b(value1, value2):
    global result_b
    result_b = value1 + value2


# Multiple return values
# Not good
def profile():
    global name
    global age
    name = "Danny"
    age = 30


def main():
    add_a(2, 4)
    #print(result_a)  # exception

    add_b(2, 4)
    print(result_b)

    profile()
    print(name)
    print(age)


if __name__ == "__main__":
    sys.exit(main())
