import sys
import collections
import enum


# defaultdict
# Unlike dict, with defaultdict you do not need to check whether a key is present or not.
def test_defaultdict():
    # case 1
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )

    favourite_colours = collections.defaultdict(list)

    for name, colour in colours:
        favourite_colours[name].append(colour)

    print(type(favourite_colours))
    print(favourite_colours)
    print(favourite_colours['Ali'])
    print(favourite_colours.get('Ali'))


# OrderedDict keeps its entries sorted as they are initially inserted. 
def test_ordereddict():
    colours = {"Red": 198, "Green": 170, "Blue": 160}
    for key, value in colours.items():
        print(key, value)

    colours = collections.OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
    for key, value in colours.items():
        print(key, value)


# Counter
def test_counter():
    colours = (
        ('Yasoob', 'Yellow'),
        ('Ali', 'Blue'),
        ('Arham', 'Green'),
        ('Ali', 'Black'),
        ('Yasoob', 'Red'),
        ('Ahmed', 'Silver'),
    )
    favs = collections.Counter(name for name, colour in colours)
    print(favs)


# deque provides you with a double ended queue
def test_deque():
    d = collections.deque()
    d.append('1')
    d.append('2')
    d.append('3')

    # like python lists
    print(len(d))
    print(d[0])
    print(d[-1])

    # pop values from both sides of the deque
    d = collections.deque(range(5))
    print(d)
    d.popleft()
    print(d)
    d.pop()
    print(d)

    # limit the amount of items
    d = collections.deque([0, 1, 2, 3, 5], maxlen=5)
    print(d)
    d.append('100')
    print(d)
    d.extend([6])
    print(d)


# namedtuple
def test_namedtuple():
    Animal = collections.namedtuple('Animal', 'name age type')
    perry = Animal(name="perry", age=31, type="cat")
    print(perry)
    print(perry.name)


# Enum
class Species(enum.Enum):
    cat = 1
    dog = 2
    horse = 3
    aardvark = 4
    butterfly = 5
    owl = 6
    platypus = 7
    dragon = 8
    unicorn = 9
    # The list goes on and on...

    # But we don't really care about age, so we can use an alias.
    kitten = 1
    puppy = 2


def test_enum():
    Animal = collections.namedtuple('Animal', 'name age type')
    tom = Animal(name="Tom", age=75, type=Species.cat)
    charlie = Animal(name="Charlie", age=2, type=Species.kitten)
    print(charlie.type == tom.type)
    print(charlie.type == Species.cat)
    print(charlie.type == Species.kitten)
    print(charlie.type)


def main():
    #test_defaultdict()
    #test_ordereddict()
    #test_counter()
    #test_deque()
    #test_namedtuple()
    test_enum()


if __name__ == "__main__":
    sys.exit(main())
