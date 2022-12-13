#!/usr/bin/env python3


import argparse
import sys
from manager import client, admin


def app():
    parser = argparse.ArgumentParser()
    excl_group = parser.add_mutually_exclusive_group()
    incl_group = parser.add_argument_group()

    excl_group.add_argument("--client", help="start as a client", action="store_true")
    excl_group.add_argument("--admin", help="start as an admin", action="store_true")
    incl_group.add_argument(
        "--filename",
        help="path to the input/output file",
        required=True,
        action="store",
    )

    args = parser.parse_args()

    try:
        if args.client:
            client.init(args.filename)
        elif args.admin:
            admin.init(args.filename)
    except KeyboardInterrupt:
        print("\n\nError: Program interrupted by user\n")
        sys.exit(1)


if __name__ == "__main__":
    app()
