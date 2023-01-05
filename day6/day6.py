import re
from typing import List

with open("./data.txt") as f:
    lines = f.read()


def get_start_of_distinct(distinct_letters_amount: int) -> int:
    pointer = 0
    while pointer + distinct_letters_amount < len(lines):
        packet = lines[pointer:(pointer + distinct_letters_amount)]
        if len(set(packet)) == distinct_letters_amount:
            pointer += distinct_letters_amount
            break
        pointer += 1
    return pointer


print(get_start_of_distinct(4))
print(get_start_of_distinct(14))
