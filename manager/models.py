#!/usr/bin/env python3


import json
import datetime
from manager.constants import SectionType


class Item:
    def __init__(self, item_id: int) -> None:
        self.id = item_id  # could also be uuid

    def to_json(self) -> str:
        return json.dumps(
            self,
            default=lambda o: o.isoformat()
            if (isinstance(o, datetime.datetime))
            else o.__dict__,
            indent=4,
        )

    def to_dict(self) -> dict:
        return json.loads(self.to_json())


class Hall(Item):
    def __init__(self, size: int, hall_id: int) -> None:
        super().__init__(hall_id)
        self.size = size

    @staticmethod
    def attributes():
        return (("id", SectionType.ID), ("size", SectionType.INT))


class Movie(Item):
    def __init__(
        self,
        movie_id: int,
        title: str,
        length: int,
        description: str,
        premiere_date: datetime.datetime,
    ) -> None:
        super().__init__(movie_id)
        self.title = title
        self.length = length
        self.description = description
        self.premiere_date = premiere_date

    @staticmethod
    def attributes():
        return (
            ("id", SectionType.ID),
            ("title", SectionType.STR),
            ("length", SectionType.INT),
            ("description", SectionType.STR),
            ("premier_date", SectionType.DATE),
        )


class Screening(Item):
    def __init__(
        self,
        screening_id: int,
        hall_id: int,
        movie_id: int,
        movie_title: str,
        date: datetime.datetime,
        available_seats: int,
    ) -> None:
        super().__init__(screening_id)
        self.hall_id = hall_id
        self.movie_id = movie_id
        self.movie_title = movie_title
        self.date = date
        self.available_seats = available_seats
        self.viewers = list()

    @staticmethod
    def attributes():
        return (
            ("id", SectionType.ID),
            ("hall_id", SectionType.HALL_ID),
            ("movie_id", SectionType.MOVIE_ID),
            ("date", SectionType.DATE),
        )
