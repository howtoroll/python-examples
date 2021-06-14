import sys


"""
https://wiki.python.org/moin/Generators
Generator functions allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.

https://www.cnblogs.com/xybaby/p/6322376.html
https://www.cnblogs.com/xybaby/p/6323358.html
"""


# Build and return a list
def firstn_func(n):
    num, nums = 0, []
    while num < n:
        nums.append(num)
        num += 1
    return nums


# Using the generator pattern (an iterable)
class firstn_iter(object):
    def __init__(self, n):
        self.n = n
        #self.num, self.nums = 0, []
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        else:
            raise StopIteration()


# a generator that yields items instead of returning a list
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


def main():
    if sys.version_info[0] < 3:
        # python2
        print "python" + str(sys.version_info[0])

        # This is clearly not acceptable in our case, because we cannot afford to keep all n "10 megabyte" integers in memory.
        #sum_of_firstn_func = sum(firstn_func(1000000))
        #print sum_of_firstn_func

        #sum_of_firstn_iter = sum(firstn_iter(1000000))
        #print sum_of_firstn_iter

        sum_of_firstn_generator = sum(firstn_generator(1000000))
        print sum_of_firstn_generator

        # Note: Python 2.x only
        # using a non-generator
        sum_of_first_n = sum(range(1000000))
        print sum_of_first_n

        # using a generator
        sum_of_first_n = sum(xrange(1000000))
        print sum_of_first_n


if __name__ == "__main__":
    sys.exit(main())
