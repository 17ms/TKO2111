from enum import Enum


class SectionType(Enum):
    ID = 1
    INT = 2
    STR = 3
    DATE = 4
    HALL_ID = 5
    MOVIE_ID = 6
    HALL_SIZE = 7
    MOVIE_TITLE = 9
    EMPTY_LIST = 10


# for strftime() & strptime()
ISO_8601_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

HALL_ATTRIB = (("id", SectionType.ID), ("size", SectionType.INT))
MOVIE_ATTRIB = (
    ("id", SectionType.ID),
    ("title", SectionType.STR),
    ("length", SectionType.INT),
    ("description", SectionType.STR),
    ("premier_date", SectionType.DATE),
)
SCREENING_ATTRIB = (
    ("id", SectionType.ID),
    ("hall_id", SectionType.HALL_ID),
    ("movie_id", SectionType.MOVIE_ID),
    ("movie_title", SectionType.MOVIE_TITLE),
    ("date", SectionType.DATE),
    ("available_seats", SectionType.HALL_SIZE),
    ("viewers", SectionType.EMPTY_LIST),
)
