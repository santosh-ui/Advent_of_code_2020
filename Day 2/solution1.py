import re
from typing import Tuple

def get_password_values(line: str) -> Tuple[int, int, str, str]:
     """Return two numbers, character and password from input"""
     match = re.match(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$", line)
     assert match is not None, "Invalid input file"

     num1str, num2str, char, password = match.groups()
     num1, num2 = int(num1str), int(num2str)
     return num1, num2, char, password


def part1() -> None:
    valid_count = 0

    with open("input.txt") as infile:
        for line in infile.readlines():
            min_count, max_count, char, password = get_password_values(line)

            char_count = password.count(char)
            if min_count <= char_count <= max_count:
                valid_count += 1

    print(valid_count)

part1()
    
