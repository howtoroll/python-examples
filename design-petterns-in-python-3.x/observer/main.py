import sys

from observer_guru import ConcreteSubject, ConcreteObserverA, ConcreteObserverB


def test_observer_guru():
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()


def main():
    test_observer_guru()


if __name__ == "__main__":
    sys.exit(main())
