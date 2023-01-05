import re
from typing import List

with open("./data.txt") as f:
    lines = f.read()


class Instruction:
    def __init__(self, amount: int, source_id: int, target_id: int):
        self.amount = amount
        self.source_id = source_id
        self.target_id = target_id


class CargoStack:
    def __init__(self, initial_cargo: List[str]):
        self.cargo = initial_cargo

    def add_one(self, cargo_ids: List[str]):
        self.cargo.append(cargo_ids)

    def add_many(self, cargo_ids: List[str]):
        self.cargo.extend(cargo_ids)

    def remove_many(self, amount: int) -> List[str]:
        removed_items = []
        for _ in range(amount):
            removed_item = self.cargo.pop()
            removed_items.append(removed_item)

        return removed_items

    def remove_many_with_same_order(self, amount: int) -> List[str]:
        cargo = self.cargo[-amount:]
        self.cargo = self.cargo[:-amount]
        return cargo


cargo_stacks_lines = lines.split("\n\n")[0].split("\n")

cargo_stacks = [CargoStack([]) for a in cargo_stacks_lines.pop() if a != ' ']

cargo_stacks_lines.reverse()
for line in cargo_stacks_lines:
    pointer = 1
    idx = 0
    while pointer < len(line):
        cargo = line[pointer]
        if cargo != ' ':
            cargo_stacks[idx].add_one(cargo)
        idx += 1
        pointer += 4

instructions_data = [re.findall(r'\d+', line) for line in lines.split("\n\n")[1].split("\n")]
instructions = [Instruction(int(data[0]), int(data[1]) - 1, int(data[2]) - 1) for data in instructions_data]
# for instruction in instructions:
#     target = cargo_stacks[instruction.target_id]
#     source = cargo_stacks[instruction.source_id]
#     cargo = source.remove_many(instruction.amount)
#     target.add_many(cargo)
#
# print(''.join([cargo.cargo[-1] for cargo in cargo_stacks]))


for instruction in instructions:
    target = cargo_stacks[instruction.target_id]
    source = cargo_stacks[instruction.source_id]
    cargo = source.remove_many_with_same_order(instruction.amount)
    target.add_many(cargo)

print(''.join([cargo.cargo[-1] for cargo in cargo_stacks]))
