import sys
from functools import reduce


# Map applies a function to all the items in an input_list.
# map(function_to_apply, list_of_inputs)
def test_map_inputs():
    items = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x**2, items))
    print(squared)


def test_map_functions():
    def multiply(x):
        return (x*x)

    def add(x):
        return (x+x)

    funcs = [multiply, add]
    for i in range(5):
        value = list(map(lambda x: x(i), funcs))
        print(value)


# Filter creates a list of elements for which a function returns true. 
def test_filter_inputs():
    number_list = range(-5, 5)
    less_than_zero = list(filter(lambda x: x < 0, number_list))
    print(less_than_zero)


# Reduce applies a rolling computation to sequential pairs of values in a list.
def test_reduce_inputs():
    product = reduce((lambda x, y: x * y), [1, 2, 3, 4])  # 1 * 2 * 3 * 4
    print(product)


def main():
    #test_map_inputs()
    #test_map_functions()

    #test_filter_inputs()

    test_reduce_inputs()


if __name__ == "__main__":
    sys.exit(main())
