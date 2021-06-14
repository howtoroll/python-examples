import sys

from factory_song_serializer import Song as Song_a, SongSerializer as SongSerializer_a
from factory_object_serializer import Song as Song_b, Movie as Movie_b, ObjectSerializer as ObjectSerializer_b
from factory_guru import client_code, ConcreteCreator1, ConcreteCreator2


def test_song_serializer():
    song_a = Song_a('1', 'Water of Love', 'Dire Straits')
    serializer = SongSerializer_a()

    print(serializer.serialize(song_a, 'JSON'))
    print(serializer.serialize(song_a, 'XML'))
    # will raise ValueError exception
    #print(serializer.serialize(song_a, 'YAML'))


def test_object_serializer():
    song_b = Song_b('1', 'Water of Love', 'Dire Straits')
    serializer = ObjectSerializer_b()

    print(serializer.serialize(song_b, 'JSON'))
    print(serializer.serialize(song_b, 'XML'))

    movie_b = Movie_b('1', 'Nomadland', 'Zhao')
    print(serializer.serialize(movie_b, 'JSON'))
    print(serializer.serialize(movie_b, 'XML'))


def test_factory_guru():
    client_code(ConcreteCreator1())
    print("\n")
    client_code(ConcreteCreator2())


def main():
    #test_song_serializer()
    #test_object_serializer()
    test_factory_guru()


if __name__ == "__main__":
    sys.exit(main())
