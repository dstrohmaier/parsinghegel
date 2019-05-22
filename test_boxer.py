"""
A small test to establish whether the parser works with tested input.
"""

from calling_boxer import parse, box


if __name__ == "__main__":
    parsed = parse("The man in the car saw the dog run across the street .\n He gave her dog biscuits .")
    result = box(parsed)

    print(result)
