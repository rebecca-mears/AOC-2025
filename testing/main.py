import argparse
import importlib
import sys
from aoc import aoc


def main():
    parser = argparse.ArgumentParser(description="Run a given AoC day module.")
    parser.add_argument("day", help="Module to load, e.g. day1")
    parser.add_argument(
        "--extension", "-e", default="txt", help="Input file extension (default: txt)"
    )
    parser.add_argument(
        "--delimiter", "-d", default=None, help="Input delimiter (default: None)"
    )

    args = parser.parse_args()

    day = importlib.import_module(args.day)

    # Get functions for both parts
    part_1 = getattr(day, "part_1")
    part_2 = getattr(day, "part_2")

    print(f"using delimiter = {args.delimiter}, extension = {args.extension}")
    run = aoc(args.day.strip("day"), delimiter=args.delimiter, file_ext=args.extension)
    run.run(part_1)
    run.run(part_2)


if __name__ == "__main__":
    main()
