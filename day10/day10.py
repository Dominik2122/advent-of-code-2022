with open("./data.txt") as f:
    instructions = f.readlines()


def solve():
    x_register = {}
    cycle = 1
    x = 1

    def save():
        x_register[cycle] = x

    for instruction in instructions:
        instruction = instruction.strip('\n')
        if instruction == 'noop':
            save()
            cycle += 1
        else:
            op, v = instruction.split()
            if op == 'addx':
                save()
                cycle += 1
                save()
                cycle += 1
                x += int(v)
            else:
                raise Exception('Unknown instruction:', instruction)

    return x_register


x_register = solve()


def part1():
    target_cycles = [20, 60, 100, 140, 180, 220]
    return sum(x_register[c] * c for c in target_cycles)


def part2():
    def overlap(pixel_pos, sprite_pos):
        return sprite_pos - 1 <= pixel_pos <= sprite_pos + 1

    CRT_WIDTH = 40
    CRT_HEIGHT = 6
    cycle = 1

    for row in range(CRT_HEIGHT):
        for pixel_pos in range(CRT_WIDTH):
            pixel = '#' if overlap(pixel_pos, x_register[cycle]) else '.'
            print(pixel, end='')
            cycle += 1

        print('')


print(part1())
print(part2())
