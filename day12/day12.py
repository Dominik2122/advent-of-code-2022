import sys

with open('data.txt') as f:
    heightmap = dict()
    min_height_pos = list()
    for y, row in enumerate(f.read().splitlines()):
        for x, h in enumerate(row):
            if h == "S":
                start, h = (x, y), "a"
                min_height_pos.append((x, y))
            elif h == "E":
                end, h = (x, y), "z"

            if h == 'a':
                min_height_pos.append((x, y))
            heightmap[(x, y)] = ord(h)


def nearest_neighbors(x, y):
    nearest_neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    return [neighbour for neighbour in nearest_neighbors if
            heightmap.get(neighbour) and (
                    heightmap.get((x, y)) + 1 >= heightmap.get(neighbour))]


def get_next(visited, distances, start, to_check):
    next_unvisited_positions = None
    min_distance = None

    if not visited.get(start):
        return start

    for position in to_check.keys():
        if not visited.get(position):
            distance = distances.get(position)
            if not min_distance:
                next_unvisited_positions = position
                min_distance = distance

            if min_distance > distance:
                next_unvisited_positions = position
                min_distance = distance
    return next_unvisited_positions

counter = []
def traverse(start, counter):
    counter.append(1)
    print(len(counter))
    visited = {}
    to_check = {start: True}
    distances = {start: 0}

    while not visited.get(end):
        position = get_next(visited, distances, start, to_check)
        distance = distances.get(position)
        neighbours = nearest_neighbors(position[0], position[1])
        for neighbour in neighbours:
            if not visited.get(neighbour):
                visited.update({neighbour: False})
                to_check.update({neighbour: True})

            if not distances.get(neighbour) or (distances.get(neighbour) >= distance and not visited.get(neighbour)):
                distances.update({neighbour: distance + 1})

        visited.update({position: True})
        del to_check[position]

    return distances.get(end)


# 1
print(traverse(start, counter))
#2
print(min([traverse(start, counter) for start in min_height_pos if start[0] == 0 or start[0] == 2]))
