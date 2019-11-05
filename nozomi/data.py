"""Represents nozomi dataclasses."""

from typing import List
from dataclasses import dataclass, field


@dataclass(frozen=True)
class MediaMetaData:
    """Metadata for a media file (i.e. an Image, Video, GIF).

    Args:
        is_video (str): Whether the media is a video type.
        imageurl (str): Url to the media file.

    """
    is_video:   str
    imageurl:   str


@dataclass(frozen=True)
class Tag:
    """Tag information.

    Args:
        tagurl (str): URL to the tag's HTML file.
        count (int): The total number of posts that have the tag.
        tagtype (str): The type of tag (i.e. character, artist, ...).
        tag (str): Name of the tag (unsanitized).
        tagname_display (str): The display name of the tag.
        sanitized_tag (str): An additional tag used for testing purposes.

    """
    tagurl:             str
    count:              int
    tagtype:            str
    tag:                str
    tagname_display:    str
    sanitized_tag:      str = field(init=False)
    def __post_init__(self):
        """Calculates fields after the object is initialized."""
        sanitized_tag = self.tagurl.split('/')[-1].split('-')[0]
        # Set the tag without raising a FrozenClass error.
        object.__setattr__(self, 'sanitized_tag', sanitized_tag)


@dataclass(frozen=True)
class Post(MediaMetaData):
    """Post information.

    Some of the fields seem rather redundant. For example, there is the field 'imageurls' but
    there will only ever be one imageurl.

    Args:
        width (int): Width of the media file.
        favorites (int): Total number of favorites.
        source (str): Site name where the media was taken from.
        date (str): #TODO: Determine if the date is the date that the post was uploaded
        height (int): Height of the media file.
        sourceid (int): #TODO: Figure out what this is.
        postid (int): The unique ID of the post.
        dataid (str): #TODO: Figure out what this is.
        general (List[Tag]): A list of the general tags that describe the post.
        copyright (List[Tag]): The various series that the media is based on.
        character (List[Tag]): The characters that are featured in the post.
        artist (List[Tag]): The artists that create the media.
        imageurls (List[MediaMetaData]): The media featured in the post.

    """
    width:      int
    favorites:  int
    source:     str
    date:       str
    height:     int
    sourceid:   int
    postid:     int
    dataid:     str
    general:    List[Tag]           = field(default_factory=list)
    copyright:  List[Tag]           = field(default_factory=list)
    character:  List[Tag]           = field(default_factory=list)
    artist:     List[Tag]           = field(default_factory=list)
    imageurls:  List[MediaMetaData] = field(default_factory=list)
