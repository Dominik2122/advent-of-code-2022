from typing import List

with open("./data.txt") as f:
    rows = f.readlines()

visible_trees = []


def check_tree_side(row: List[str], height: int):
    visible = True
    for side_tree_height in row:
        if int(side_tree_height) >= int(height):
            visible = False
            break
    if visible:
        visible_trees.append((x_index, y_index))
    return visible


for y_index, row in enumerate(rows):
    row = list(row.strip('\n'))
    for x_index, height in enumerate(row):
        if y_index == 0 or y_index == len(rows) - 1 or x_index == 0 or x_index == len(row) - 1:
            visible_trees.append((x_index, y_index))
            continue
        if not check_tree_side(row[:x_index], height):
            if not check_tree_side(row[x_index + 1:], height):
                column = [line[x_index] for line in rows]
                if not check_tree_side(column[:y_index], height):
                    check_tree_side(column[y_index + 1:], height)

print(len(visible_trees))


def check_tree_side_with_count(row: List[str], height: int):
    counter = 0
    for side_tree_height in row:
        counter += 1
        if int(side_tree_height) >= int(height):
            break

    return counter


biggest_result = 0
for y_index, row in enumerate(rows):
    row = list(row.strip('\n'))
    for x_index, height in enumerate(row):
        if y_index == 0 or y_index == len(rows) - 1 or x_index == 0 or x_index == len(row) - 1:
            continue

        left_row = row[:x_index]
        left_row.reverse()
        left = check_tree_side_with_count(left_row, height)
        right = check_tree_side_with_count(row[x_index + 1:], height)
        column = [line[x_index] for line in rows]


        top_row = column[:y_index]
        top_row.reverse()
        top = check_tree_side_with_count(top_row, height)

        bottom = check_tree_side_with_count(column[y_index + 1:], height)
        result = left * right * top * bottom
        print(left, right, top, bottom)
        if result > biggest_result:
            biggest_result = result

print(biggest_result)
