import os

origin_x = 0
origin_y = 0
destination_x = 0
destination_y = 0

heights = []
known_steps = []

def climb(x, y, seen):
    minimum = float('inf')

    if x == destination_x and y == destination_y:
        return 0

    seen.append((x, y))

    cur_height = heights[y][x]
    up = float('inf')
    down = float('inf')
    left = float('inf')
    right = float('inf')

    if y - 1 >= 0 and (x, y - 1) not in seen and heights[y - 1][x] <= cur_height + 1:
        if known_steps[y][x][0] is not None:
            up = known_steps[y][x][0]
        else:
            up = climb(x, y - 1, seen) + 1
            known_steps[y][x][0] = up

    if y + 1 < len(heights) and (x, y + 1) not in seen and heights[y + 1][x] <= cur_height + 1:
        if known_steps[y][x][1] is not None:
            down = known_steps[y][x][1]
        else:
            down = climb(x, y + 1, seen) + 1
            known_steps[y][x][1] = down

    if x - 1 >= 0 and (x - 1, y) not in seen and heights[y][x - 1] <= cur_height + 1:
        if known_steps[y][x][2] is not None:
            left = known_steps[y][x][2]
        else:
            left = climb(x - 1, y, seen) + 1
            known_steps[y][x][2] = left

    if x + 1 < len(heights[0]) and (x + 1, y) not in seen and heights[y][x + 1] <= cur_height + 1:
        if known_steps[y][x][3] is not None:
            right = known_steps[y][x][3]
        else:
            right = climb(x + 1, y, seen) + 1
            known_steps[y][x][3] = right

    minimum = min([up, down, left, right])

    seen.pop()
    return minimum

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for row in range(0, len(lines)):
    line = lines[row].strip()
    if line == '':
        continue

    heights.append([])
    known_steps.append([])

    for col in range(0, len(line)):
        if line[col] == 'S':
            origin_x = col
            origin_y = row
            heights[row].append(1)
        elif line[col] == 'E':
            destination_x = col
            destination_y = row
            heights[row].append(26)
        else:
            heights[row].append(ord(line[col]) - 96)
        known_steps[row].append([None for _ in range(0, 4)])

min_steps = climb(origin_x, origin_y, [])

print(min_steps)
