import sys


# *args is used to send a non-keyworded variable length argument list to the function.
def test_args(f_arg, *args):
    print("first normal arg:", f_arg)
    for arg in args:
        print("another arg through *args:", arg)


def test_args_to_call_function(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)


# **kwargs allows you to pass keyworded variable length of arguments to a function.
def test_kwargs(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


def test_kwargs_to_call_function(arg1, arg2, arg3):
    print("arg1:", arg1)  # get value by key arg1
    print("arg2:", arg2)
    print("arg3:", arg3)


def formal_order(fargs, *args, **kwargs):
    pass


def main():
    #test_args('yasoob', 'python', 'eggs', 'test')
    args = ("two", 3, 5)  # is a tuple
    test_args_to_call_function(*args)

    #test_kwargs(n1="yasoob", n2="python")
    kwargs = {"arg3": 3, "arg2": "two", "arg1": 5}
    test_kwargs_to_call_function(**kwargs)


if __name__ == "__main__":
    sys.exit(main())
