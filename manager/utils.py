#!/usr/bin/env python3


import json
from datetime import datetime
from tabulate import tabulate
from manager import constants
from manager.constants import ISO_8601_DATE_FORMAT, SectionType


def read_json(filename: str) -> dict:
    try:
        with open(filename, "r", encoding="utf-8") as handle:
            # could check for expired screenings at this point
            return json.load(handle)
    except FileNotFoundError:
        data = {}
        data["halls"] = {}
        data["movies"] = {}
        data["screenings"] = {}

        return data


def write_json(filename: str, data: dict) -> None:
    with open(filename, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=4)


def print_list(dataset: list) -> None:
    if len(dataset) == 0:
        print("[ No data to display ]")
        return

    for item in dataset:
        if "description" in item:
            item["description"] = item["description"][:40] + "..."
        if "viewers" in item and len(item["viewers"]) > 3:
            item["viewers"] = (
                ", ".join(item["viewers"][:3])
                + " and "
                + str(len(item["viewers"]) - 1)
                + " others"
            )
        elif "viewers" in item:
            item["viewers"] = ", ".join(item["viewers"])

    headers = dataset[0].keys()
    rows = [x.values() for x in dataset]
    print(tabulate(rows, headers, tablefmt="psql"))


def add_item(data: dict, section: str) -> None:
    datasection = data[section]

    if section == "halls":
        attributes = constants.HALL_ATTRIB
    elif section == "movies":
        attributes = constants.MOVIE_ATTRIB
    elif section == "screenings":
        attributes = constants.SCREENING_ATTRIB

    item = {}
    id_key = int([*data[section].keys()][-1]) + 1

    for attr in attributes:
        get_input(data, attr, id_key, item)

    datasection[str(id_key)] = item


def get_input(data: dict, attr: tuple, id_key: int, item: dict) -> None:
    # try until input is valid
    while True:
        try:
            if attr[1] == SectionType.ID:
                item[attr[0]] = id_key
            elif attr[1] == SectionType.INT:
                item[attr[0]] = int(input(f"{attr[0]} {attr[1].name} > "))
            elif attr[1] == SectionType.DATE:
                date = datetime.strptime(
                    input(f"{attr[0]} ({attr[1].name}: {ISO_8601_DATE_FORMAT}) > "),
                    ISO_8601_DATE_FORMAT,
                )
                item[attr[0]] = datetime.strftime(date, ISO_8601_DATE_FORMAT)
            elif attr[1] == SectionType.MOVIE_ID:
                item[attr[0]] = int(input(f"{attr[0]} {attr[1].name} > "))
            elif attr[1] == SectionType.HALL_ID:
                item[attr[0]] = int(input(f"{attr[0]} {attr[1].name} > "))
            elif attr[1] == SectionType.HALL_SIZE:
                item["available_seats"] = data["halls"][str(item["hall_id"])]["size"]
            elif attr[1] == SectionType.MOVIE_TITLE:
                item["movie_title"] = data["movies"][str(item["movie_id"])]["title"]
            elif attr[1] == SectionType.EMPTY_LIST:
                item[attr[0]] = []
            else:
                item[attr[0]] = input(f"{attr[0]} ({attr[1].name}) > ")
            break
        except ValueError:
            print("\n[ Invalid value or format, please try again ]\n")


def edit_item(datasection: dict, item_id: str, field_key: str) -> None:
    if field_key not in datasection[item_id]:
        raise KeyError

    new_val = input(f"{field_key} > ")
    datasection[item_id][field_key] = new_val

    print(f"\n[ Field '{field_key}' of item '{item_id}' successfully updated ]")


def delete_item(data: dict, section: str, item_id: str) -> None:
    del data[section][item_id]
    print(f"[ Item '{item_id}' successfully deleted from '{section}' ]")

    if section in ("movies", "halls"):
        amount = delete_relations(data["screenings"], section, item_id)
        print(f"[ {amount} relations from 'screenings' deleted ]")


def delete_relations(screenings: dict, section: str, item_id: str) -> int:
    field_key = "movie_id" if section == "movies" else "hall_id"
    deletion_keys = list()
    count = 0

    for screening_id, screening in screenings.items():
        if screening[field_key] == int(item_id):
            deletion_keys.append(screening_id)
            count += 1

    for del_key in deletion_keys:
        del screenings[del_key]

    return count


def book_ticket(data: dict, screening_id: str, viewer: str) -> None:
    screening = data["screenings"][screening_id]

    if not int(screening["available_seats"]):
        print("[ Can't book a ticket, the selected screening is full ]")
        return

    screening["available_seats"] = int(screening["available_seats"]) - 1
    data["screenings"][screening_id]["viewers"].append(viewer)

    title = data["movies"][str(screening["movie_id"])]["title"]
    date = screening["date"]

    print(f"[ Ticket for '{viewer}' successfully booked to '{title}' {date} ]")
