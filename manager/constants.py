from enum import Enum


# for strftime() & strptime()
ISO_8601_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"


class SectionType(Enum):
    ID = 1
    INT = 2
    STR = 3
    DATE = 4
    HALL_ID = 5
    MOVIE_ID = 6
