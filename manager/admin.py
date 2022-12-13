#!/usr/bin/env python3


import copy
import sys
from manager import utils


def init(filename: str):
    data = utils.read_json(filename)
    print("\n[ Admin initialized ]\n\n")

    while True:
        cmd_in = input("> ")

        print("")
        parse(cmd_in, data, filename)
        print("")


def parse(cmd_in: str, data: dict, filename: str) -> dict:
    parts = cmd_in.strip().lower().split(" ")

    try:
        if parts[0] == "quit":
            print("[ Quitting... ]\n")
            sys.exit(0)
        elif parts[0] == "list":
            # deepcopy of data to prevent unwanted modifications
            dataset = copy.deepcopy(list(data[parts[1]].values()))
            utils.print_list(dataset)
        elif parts[0] == "add":
            utils.add_item(data, parts[1])
        elif parts[0] == "edit":
            datasection = data[parts[1]]
            utils.edit_item(datasection, parts[2], parts[3])
        elif parts[0] == "delete":
            utils.delete_item(data, parts[1], parts[2])
        elif parts[0] == "help":
            print_usage()
        else:
            print("[ Invalid command, please try again ]")
    except IndexError:
        print("[ Missing arguments, please try again ]")
    except KeyError:
        print("[ Invalid argument, please try again ]")

    utils.write_json(filename, data)
    return data


def print_usage() -> None:
    print(
        """usage: [list | add | edit | delete | help | quit] <ARGUMENTS>

commands:
  list      SECTION             list all data entries of a section
  add       SECTION             add a new entry into a section
  edit      SECTION ID FIELD    edit a field of a section entry
  delete    SECTION ID          delete an entry from a section
  help                          show this help message
  quit                          exit the app"""
    )
