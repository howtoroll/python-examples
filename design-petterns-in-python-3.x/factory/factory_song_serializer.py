import json
import xml.etree.ElementTree as et


class Song:
    def __init__(self, song_id, title, artist):
        self.song_id = song_id
        self.title = title
        self.artist = artist


"""
Complex logical code uses if/elif/else structures to change the behavior of an application.
The serialize() method in SongSerializer will require changes for many different reasons.
"""
# class SongSerializer:
#     def serialize(self, song, format):
#         if format == 'JSON':
#             song_info = {
#                 'id': song.song_id,
#                 'title': song.title,
#                 'artist': song.artist
#             }
#             return json.dumps(song_info)
#         elif format == 'XML':
#             song_info = et.Element('song', attrib={'id': song.song_id})
#             title = et.SubElement(song_info, 'title')
#             title.text = song.title
#             artist = et.SubElement(song_info, 'artist')
#             artist.text = song.artist
#             return et.tostring(song_info, encoding='unicode')
#         else:
#             raise ValueError(format)


"""
The ideal situation would be if any of those changes in requirements could be implemented without changing the .serialize() method.
"""
# client
class SongSerializer:
    def serialize(self, song, out_format):
        serializer = get_serializer(out_format)
        return serializer(song)


# creator
def get_serializer(out_format):
    if out_format == 'JSON':
        return serialize_to_json
    elif out_format == 'XML':
        return serialize_to_xml
    else:
        raise ValueError(out_format)


# product
def serialize_to_xml(song):
    song_element = et.Element('song', attrib={'id': song.song_id})
    title = et.SubElement(song_element, 'title')
    title.text = song.title
    artist = et.SubElement(song_element, 'artist')
    artist.text = song.artist
    return et.tostring(song_element, encoding='unicode')


# product
def serialize_to_json(song):
    payload = {
        'id': song.song_id,
        'title': song.title,
        'artist': song.artist
    }
    return json.dumps(payload)
