class Position:
    def __init__(self, x_axis: int, y_axis: int):
        self.x_axis = x_axis
        self.y_axis = y_axis

    def calculate_x_axis_diff(self, other_pos: 'Position'):
        return abs(self.x_axis - other_pos.x_axis)

    def calculate_y_axis_diff(self, other_pos: 'Position'):
        return abs(self.y_axis - other_pos.y_axis)

    def create_new_with_updated_position(self, x_axis_diff: int, y_axis_diff: int):
        return Position(self.x_axis + x_axis_diff, self.y_axis + y_axis_diff)

    def copy(self):
        return Position(self.x_axis, self.y_axis)


class NextKnotPosition(Position):

    def is_equal(self, other_position: Position):
        return self.calculate_x_axis_diff(other_position) == 0 and self.calculate_y_axis_diff(other_position) == 0

    def copy(self):
        return NextKnotPosition(self.x_axis, self.y_axis)

    def create_position_after_previous(self, x_axis_diff: int, y_axis_diff: int, previous_knot: Position,
                                       previous_knot_copy):
        if self.is_equal(previous_knot):
            return self

        if self.calculate_x_axis_diff(previous_knot) + self.calculate_y_axis_diff(previous_knot) == 1:
            return self

        if (self.calculate_x_axis_diff(previous_knot) == 2 and self.calculate_y_axis_diff(previous_knot) == 0) or (
                self.calculate_x_axis_diff(previous_knot) == 0 and self.calculate_y_axis_diff(previous_knot) == 2):
            position = self.create_new_with_updated_position(x_axis_diff, y_axis_diff)
            return NextKnotPosition(position.x_axis, position.y_axis)

        if self.calculate_x_axis_diff(previous_knot) == 1 and self.calculate_y_axis_diff(previous_knot) == 1:
            return self

        else:
            return NextKnotPosition(previous_knot_copy.x_axis, previous_knot_copy.y_axis)


with open("./data.txt") as f:
    instructions = f.readlines()


def process_instruction(head_position: Position, other_positions, instructions):
    positions_visited = {head_position.x_axis: {head_position.y_axis}}
    for instruction in instructions:
        instruction = instruction.strip('\n').split(' ')
        for i in range(int(instruction[1])):
            x_axis_diff = 0
            y_axis_diff = 0
            if instruction[0] == 'R':
                x_axis_diff = 1
            elif instruction[0] == 'L':
                x_axis_diff = -1
            elif instruction[0] == 'U':
                y_axis_diff = 1
            else:
                y_axis_diff = -1
            head_previous_position = head_position.copy()
            head_position = head_position.create_new_with_updated_position(x_axis_diff, y_axis_diff)
            other_positions_copy = [knot.copy() for knot in other_positions]
            print(instruction)
            print('HEAD', head_position.x_axis, head_position.y_axis)
            for id, knot in enumerate(other_positions):
                if id == 0:
                    previous_knot = head_position
                    previous_knot_previous_position = head_previous_position
                else:
                    previous_knot = other_positions[id - 1]
                    previous_knot_previous_position = other_positions_copy[id - 1]

                other_positions[id] = knot.create_position_after_previous(x_axis_diff, y_axis_diff, previous_knot,
                                                                          previous_knot_previous_position)
                print(id+1, other_positions[id].x_axis, other_positions[id].y_axis)
                if id == (len(other_positions) - 1):
                    if not positions_visited.get(knot.x_axis):
                        positions_visited[knot.x_axis] = {knot.y_axis}
                    else:
                        positions_visited[knot.x_axis].add(knot.y_axis)

    return positions_visited


# head_position = Position(0, 0)
# tail_position = NextKnotPosition(0, 0)
# task_one = process_instruction(head_position, [tail_position], instructions)
# pos = []
# for x_pos in task_one:
#     pos.extend(task_one.get(x_pos))
#
# print(len(pos))

head_position_two = Position(0, 0)
knots = [NextKnotPosition(0, 0) for _ in range(9)]
task_two = process_instruction(head_position_two, knots, instructions)
pos_two = []
for x_pos in task_two:
    pos_two.extend(task_two.get(x_pos))
print(len(pos_two))
