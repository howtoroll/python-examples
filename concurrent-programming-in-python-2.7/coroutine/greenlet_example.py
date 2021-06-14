import sys
from greenlet import greenlet


def simpleUse():
    def test1():
        print 12
        gr2.switch()
        print 34

    def test2():
        print 56
        gr1.switch()
        print 78

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()


def simpleUseWithMsg():
    def test1():
        print 12
        y = gr2.switch(56)
        print y

    def test2(x):
        print x
        gr1.switch(34)
        print 78

    gr1 = greenlet(test1)
    gr2 = greenlet(test2)
    gr1.switch()


def main():
    simpleUse()


if __name__ == "__main__":
    sys.exit(main())
