import sys

from facade_simple import FacadeClient as facade_a
from facade_weather import FacadeClient as facade_b
from facade_github import generate_changelog
from facade_guru import *


def test_facade_simple():
    client = facade_a()
    client.ask_even_organizer()


def test_facade_weather():
    client = facade_b()
    client.ask_forecast()


def test_facade_github():
    changelog = generate_changelog('busy-beaver-dev', 'busy-beaver', '2.9.0')
    print(changelog)


def test_facade_guru():
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)


def main():
    #test_facade_simple()
    #test_facade_weather()
    #test_facade_github()
    test_facade_guru()


if __name__ == "__main__":
    sys.exit(main())
