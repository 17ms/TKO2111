#!/usr/bin/env python3


import random
from urllib import request
from datetime import datetime, timedelta
from manager import constants


WORDLIST_URL = "https://www.mit.edu/~ecprice/wordlist.10000"


def request_wordlist() -> [str]:
    res = request.urlopen(WORDLIST_URL)
    content = res.read().decode("utf-8")

    return content.splitlines()


def generate_testdata() -> dict:
    words = request_wordlist()
    now = datetime.now()

    data = dict()
    data["halls"] = dict()
    data["movies"] = dict()
    data["screenings"] = dict()

    for i in range(5):
        title = " ".join([words[random.randint(0, len(words) - 1)] for _ in range(3)])
        description = " ".join(
            [words[random.randint(0, len(words) - 1)] for _ in range(20)]
        )
        premiere_date = datetime.strftime(
            datetime(
                random.randint(1900, 2020), random.randint(1, 12), random.randint(1, 28)
            ),
            constants.ISO_8601_DATE_FORMAT,
        )

        data["halls"][str(i)] = {"id": i, "size": random.randint(50, 350)}
        data["movies"][str(i)] = {
            "id": i,
            "title": title,
            "length": random.randint(60, 240),
            "description": description,
            "premiere_date": premiere_date,
        }
    for i in range(20):
        hall = data["halls"][str(random.randint(0, len(data["halls"]) - 1))]
        movie = data["movies"][str(random.randint(0, len(data["movies"]) - 1))]
        date = datetime.strftime(
            now + timedelta(days=random.randint(1, 100)), constants.ISO_8601_DATE_FORMAT
        )

        screening = {
            "id": i,
            "hall_id": hall["id"],
            "movie_id": movie["id"],
            "movie_title": movie["title"],
            "date": date,
            "available_seats": hall["size"],
            "viewers": [],
        }

        for _ in range(random.randint(0, 15)):
            screening["viewers"].append(words[random.randint(0, len(words) - 1)])

        data["screenings"][str(i)] = screening

    return data
