with open("./data.txt") as f:
    lines = f.read()


def sort_most_calories():
    most_calories = 0
    current_elf_load = 0
    elves_load = lines.split('\n')
    elves_load_added = []
    for load in elves_load:
        if load:
            current_elf_load += int(load)
        else:
            elves_load_added.append(current_elf_load)
            current_elf_load = 0
    return sorted(elves_load_added)


print(sort_most_calories()[-1])
print(sort_most_calories()[-1] + sort_most_calories()[-2] + sort_most_calories()[-3])
