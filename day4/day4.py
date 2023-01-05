import string

with open("./data.txt") as f:
    lines = f.readlines()


def assignment_collide(assignment_a, assignment_b_start, assignment_b_end):
    return int(assignment_b_start) <= int(assignment_a) <= int(assignment_b_end)


fully_contained = 0
for pair in lines:
    first_assignment, second_assignment = pair.split(',')
    first_assignment_start, first_assignment_end = first_assignment.split('-')
    second_assignment_start, second_assignment_end = second_assignment.split('-')
    if assignment_collide(first_assignment_start, second_assignment_start, second_assignment_end) or assignment_collide(
            first_assignment_end, second_assignment_start, second_assignment_end) or assignment_collide(
        second_assignment_start, first_assignment_start, first_assignment_end) or assignment_collide(
        second_assignment_end,
        first_assignment_start,
        first_assignment_end):
        fully_contained += 1

print(fully_contained)
