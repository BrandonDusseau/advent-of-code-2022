import os

cave = []
paths = []
min_x = float('inf')
max_x = 0
max_y = 0
left_shift = 0

def prepend_column():
    global min_x
    global max_x
    global left_shift
    for row in range(0, len(cave)):
        cave[row].insert(0, '#' if row == len(cave) - 1 else '.')
    min_x += 1
    max_x += 1
    left_shift += 1

def append_column():
    for row in range(0, len(cave)):
        cave[row].append('#' if row == len(cave) - 1 else '.')

def drop_sand():
    sand_x = 500 + left_shift - min_x + left_shift
    sand_y = 0
    next_x = sand_x
    next_y = sand_y

    if cave[sand_y][sand_x] == 'o':
        return False

    rest = False
    while not rest:
        if next_x + 1 >= len(cave[0]):
            append_column()
        elif next_x - 1 < 0:
            prepend_column()
            next_x += 1
            sand_x += 1

        if cave[next_y + 1][next_x] == '.':
            next_y = next_y + 1
        elif next_x - 1 < 0 or cave[next_y + 1][next_x - 1] == '.':
            next_y = next_y + 1
            next_x = next_x - 1
        elif next_x + 1 >= len(cave[0]) or cave[next_y + 1][next_x + 1] == '.':
            next_y = next_y + 1
            next_x = next_x + 1
        else:
            rest = True

        # if not rest:
        #     visualize(next_x, next_y)

    cave[next_y][next_x] = 'o'
    return True

def visualize(sand_x=None, sand_y=None):
    for row in range(0, len(cave)):
        cols = cave[row].copy()
        if row == sand_y:
            cols[sand_x] = '*'
        print(''.join(cols))
    print()

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    path = line.split(' -> ')
    parsed_points = []
    for point in path:
        (x, y) = [int(p) for p in point.split(',')]
        if x < min_x:
            min_x = x
            min_x_y = y
        if x > max_x:
            max_x = x
            max_x_y = y
        if y > max_y:
            max_y = y
        parsed_points.append((x, y))
    paths.append(parsed_points)

floor_level = max_y + 2

for row in range(0, floor_level + 1):
    cave.append([])
    for col in range(min_x, max_x + 1):
        if row == max_y + 2:
            cave[row].append('#')
        else:
            cave[row].append('+' if row == 0 and col == 500 else '.')

for path in paths:
    last_point = path[0]
    for point in range(1, len(path)):
        (last_x, last_y) = last_point
        (dest_x, dest_y) = path[point]
        x_range = range(last_x, dest_x + 1)
        if last_x > dest_x:
            x_range = range(last_x, dest_x - 1, - 1)
        y_range = range(last_y, dest_y + 1)
        if last_y > dest_y:
            y_range = range(last_y, dest_y - 1, - 1)

        for x in x_range:
            for y in y_range:
                x_place = x - min_x
                cave[y][x_place] = '#'
        last_point = (dest_x, dest_y)

sand_can_fall = True
units_fallen = 0
while sand_can_fall:
    sand_can_fall = drop_sand()
    if sand_can_fall:
        units_fallen += 1

visualize()
print(units_fallen)