with open("./data.txt") as f:
    lines = f.read()


def sort_most_calories():
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


sorted_elf_load = sort_most_calories()
print(sorted_elf_load[-1])
print(sorted_elf_load[-1] + sorted_elf_load[-2] + sorted_elf_load[-3])
