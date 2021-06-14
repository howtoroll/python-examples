import sys

from singleton_by_class_variable import SingleTon as singleton_a
from singleton_by_import import singleton_instance as singleton_b
from singleton_by_metaclass import Singleton as singleton_c
from singleton_by_new_v1 import SingleTon as singleton_d
from singleton_by_new_v2 import SingleTon as singleton_e


def test_singleton_by_class_variable():
    intance_a = singleton_a.get_instance()
    intance_b = singleton_a.get_instance()
    intance_c = singleton_a.instance
    print(f"test_singleton_by_class_variable: id of a is {intance_a.get_id()}")
    print(f"test_singleton_by_class_variable: id of b is {intance_b.get_id()}")
    print(f"test_singleton_by_class_variable: id of c is {intance_c.get_id()}")


def test_singleton_by_import():
    print(f"test_singleton_by_import (main.py): id is {singleton_b.get_id()}")


def test_singleton_by_metaclass():
    intance_a = singleton_c()
    intance_b = singleton_c()
    print(f"test_singleton_by_metaclass: id of a is {intance_a.get_id()}")
    print(f"test_singleton_by_metaclass: id of b is {intance_b.get_id()}")


def test_singleton_by_new_v1():
    intance_a = singleton_d()
    intance_b = singleton_d()
    print(f"test_singleton_by_new_v1: id of a is {intance_a.get_id()}")
    print(f"test_singleton_by_new_v1: id of b is {intance_b.get_id()}")


def test_singleton_by_new_v2():
    intance_a = singleton_e()
    intance_b = singleton_e()
    print(f"test_singleton_by_new_v2: id of a is {intance_a.get_id()}")
    print(f"test_singleton_by_new_v2: id of b is {intance_b.get_id()}")


def main():
    test_singleton_by_class_variable()
    test_singleton_by_import()
    test_singleton_by_metaclass()
    test_singleton_by_new_v1()
    test_singleton_by_new_v2()


if __name__ == "__main__":
    sys.exit(main())
