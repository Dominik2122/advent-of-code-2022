import functools
from typing import List


class Monkey:
    def __init__(self, id: int, starting_items: List[int], operation, test, positive, negative, worry_divisor):
        self.id = id
        self.starting_items = starting_items
        self.next_round_items = []
        self.operation = operation
        self.test = test
        self.positive = positive
        self.negative = negative
        self.operation_count = 0
        self.worry_divisor = worry_divisor

    def get_operation_result(self):
        if not len(self.starting_items):
            return
        self.operation_count += 1
        old = self.pop_item()
        new = eval(self.operation)
        return new // self.worry_divisor

    def make_test(self, value):
        return self.positive if value % self.test == 0 else self.negative

    def pop_item(self):
        return self.starting_items.pop(0)

    def add_item(self, item):
        return self.starting_items.append(item)


def monkey_factory(instruction, worry_divisor):
    monkey_instructions = instruction.split('\n\n')
    monkeys = []
    for id, monkey_instruction in enumerate(monkey_instructions):
        monkey_instruction = monkey_instruction.split('\n')
        monkey_id = id
        starting_items = [int(n) for n in monkey_instruction[1].strip('  Starting items: ').split(', ')]
        operation = 'o' + monkey_instruction[2].strip('Operation: new =')
        test = int(monkey_instruction[3].strip('Test: divisible by '))
        positive = int(monkey_instruction[4].strip('If true: throw to monkey '))
        negative = int(monkey_instruction[5].strip('If false: throw to monkey'))
        monkey = Monkey(monkey_id, starting_items, operation, test, positive, negative, worry_divisor)
        monkeys.append(monkey)
    return monkeys


class MonkeyGame:

    def __init__(self, monk):
        common_worry_divisor = functools.reduce(lambda cd, x: cd * x, (m.test for m in monkeys))
        self.monkeys: List[Monkey] = monk
        self.current_monkey = None
        self.common_worry_divisor = common_worry_divisor

    def make_round(self):
        for monkey in self.monkeys:
            while len(monkey.starting_items) != 0:
                item = monkey.starting_items[0]
                result = monkey.get_operation_result()
                if result:
                    result = result % self.common_worry_divisor
                    next_monkey_id = monkey.make_test(result)
                    self.monkeys[next_monkey_id].add_item(result)


with open("./test_data.txt") as f:
    test_instruction = f.read()

with open("./data.txt") as f:
    instructions = f.read()

monkeys = monkey_factory(instructions, 1)
monkey_game = MonkeyGame(monkeys)
for round in range(10000):
    monkey_game.make_round()
first, second = sorted([monkey.operation_count for monkey in monkey_game.monkeys])[-2:]
print(first*second)
