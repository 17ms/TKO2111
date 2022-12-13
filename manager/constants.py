from enum import Enum


# for strftime() & strptime()
ISO_8601_DATE_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

# random data for tests
WORDLIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"


class SectionType(Enum):
    ID = 1
    INT = 2
    STR = 3
    DATE = 4
    HALL_ID = 5
    MOVIE_ID = 6
