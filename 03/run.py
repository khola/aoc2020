import math as m

with open("input", "r") as file:
    pattern = file.read().splitlines()

width = len(pattern[0])


def traverse(step_x, step_y=1):
    offset_x = 0
    trees = 0
    for row_index in range(1, m.ceil(len(pattern) / step_y)):
        offset_x += step_x
        pattern_x = offset_x % width
        if pattern[row_index * step_y][pattern_x] == "#":
            trees += 1
    return trees


print(traverse(1) * traverse(3) * traverse(5) * traverse(7) * traverse(1, 2))
