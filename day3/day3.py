import string

with open("./data.txt") as f:
    lines = f.readlines()
numbers = {}
for char in list(string.ascii_lowercase):
    numbers[char] = ord(char) - 96

for char in list(string.ascii_uppercase):
    numbers[char] = ord(char) - 38


def divide_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


score = 0
for rucksack in lines:
    container_a, container_b = divide_list(rucksack)
    score += numbers[list(set(container_a) & set(container_b))[0]]

print(score)

score = 0
for index, rucksack in enumerate(lines):
    if index % 3 != 0:
        continue
    score += numbers[list(set(rucksack) & set(lines[index + 1].strip()) & set(lines[index + 2].strip()))[0]]
print(score)
