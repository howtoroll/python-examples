import sys
from functools import wraps


# Decorators
def a_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


def a_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


def b_new_decorator(a_func):

    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@b_new_decorator
def b_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


def c_new_decorator(c_func):

    @wraps(c_func)
    def wrapTheFunction(*args, **kwargs):
        print(c_func.__name__ + " was called")
        print("I am doing some boring work before executing a_func()")
        c_func(*args, **kwargs)
        print("I am doing some boring work after executing a_func()")

    return wrapTheFunction


@c_new_decorator
def c_function_requiring_decoration():
    print("I am the function which needs some decoration to remove my foul smell")


# Decorators with Arguments
def logit(logfile='out1.log'):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called"
            print(log_string)
            print(logfile)
            #with open(logfile, 'a') as opened_file:
            #    opened_file.write(log_string + '\n')
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator


@logit()
def myfunc1():
    pass


@logit(logfile='out2.log')
def myfunc2():
    pass


# Decorator Classes
class Logit:

    LOG_FILE = 'out1.log'

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        log_string = self.func.__name__ + " was called"
        print(log_string)
        print(self.LOG_FILE)
        #with open(self._logfile, 'a') as opened_file:
        #    opened_file.write(log_string + '\n')

        self.notify()

        return self.func(*args, **kwargs)

    def notify(self):
        pass


class EmailLogit(Logit):
    def __init__(self, func, email='admin@myproject.com', *args, **kwargs):
        self.email = email
        super(EmailLogit, self).__init__(func, *args, **kwargs)

    def notify(self):
        print("send email")


Logit.LOG_FILE = 'out2.log'  # if change log file


@Logit
def myfunc3():
    pass


@EmailLogit
def myfunc4():
    pass


def main():
    # Decorators
    #a1 = a_new_decorator(a_function_requiring_decoration)
    #a1()

    #b1 = b_function_requiring_decoration
    #b1()
    #print(b_function_requiring_decoration.__name__)

    #c1 = c_function_requiring_decoration
    #c1()
    #print(c_function_requiring_decoration.__name__)

    # Decorators with Arguments
    #myfunc1()
    #myfunc2()

    # Decorator Classes
    myfunc3()
    myfunc4()


if __name__ == "__main__":
    sys.exit(main())
