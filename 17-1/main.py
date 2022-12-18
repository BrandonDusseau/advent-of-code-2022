import os

directions = []

rocks = [
    [['@', '@', '@', '@']],

    [[None, '@', None],
     ['@', '@', '@'],
     [None, '@', None]],

    [[None, None, '@'],
     [None, None, '@'],
     ['@', '@', '@']],

    [['@'],
     ['@'],
     ['@'],
     ['@']],

    [['@', '@'],
     ['@', '@']],
]

rock_left_boundaries = [
    [0],
    [1, 0, 1],
    [2, 2, 0],
    [0, 0, 0 ,0],
    [0, 0]
]

rock_right_boundaries = [
    [3],
    [1, 2, 1],
    [2, 2, 2],
    [0, 0, 0 ,0],
    [1, 1]
]

rock_bottom_boundaries = [
    [0, 0, 0, 0],
    [1, 2, 1],
    [2, 2, 2],
    [3],
    [1, 1]
]

rock_top_left_x = 2
rock_top_left_y = 0
current_rock = 0
current_iteration = 0

map = []

def visualize(full_tower=False):
    display_range = range(max(0, rock_top_left_y - 10), min(len(map), rock_top_left_y + 13))
    if full_tower:
        display_range = range(0, len(map))
    for row in display_range:
        row_string = ''.join(map[row])
        print(f'|{row_string}|')

    if full_tower or rock_top_left_y + 13 >= len(map):
        print('+-------+')
    print()

def increase_size(height):
    for _ in range(0, height):
        map.insert(0, ['.' for _ in range(0, 7)])

def get_current_rock_shape():
    return rocks[current_rock % len(rocks)]

def insert_rock():
    global rock_top_left_x
    global rock_top_left_y

    increase_size(3)
    rock = get_current_rock_shape()
    increase_size(len(rock))

    rock_edge = None
    for rock_col in range(0, len(rock[0])):
        if rock_edge is not None:
            break

        for rock_row in range(0, len(rock)):
            if rock[rock_row][rock_col] == '@':
                rock_edge = rock_col
                break

    rock_top_left_x = rock_edge + 2
    rock_top_left_y = 0

    for rock_row in range(0, len(rock)):
        for rock_col in range(0, len(rock[0])):
            if rock[rock_row][rock_col] == '@':
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] = '@'

def solidify_rock():
    global current_rock
    rock = get_current_rock_shape()
    for rock_row in range(0, len(rock)):
        for rock_col in range(0, len(rock[0])):
            if rock[rock_row][rock_col] == '@':
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] = '#'
    current_rock += 1

def move_rock_left():
    global rock_top_left_x
    rock = get_current_rock_shape()
    left_boundaries = rock_left_boundaries[current_rock % len(rocks)]

    for rock_row in range(0, len(rock)):
        left_edge = rock_top_left_x + left_boundaries[rock_row]
        map_row = rock_top_left_y + rock_row
        if left_edge - 1 < 0 or map[map_row][left_edge - 1] == '#':
            return False

    for rock_row in range(0, len(rock)):
        for rock_col in range(0, len(rock[0])):
            cur_symbol = rock[rock_row][rock_col]
            if cur_symbol is not None:
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col - 1] = cur_symbol
            if map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] == '@':
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] = '.'

    rock_top_left_x -= 1
    return True

def move_rock_right():
    global rock_top_left_x
    rock = get_current_rock_shape()
    right_boundaries = rock_right_boundaries[current_rock % len(rocks)]

    for rock_row in range(0, len(rock)):
        right_edge = rock_top_left_x + right_boundaries[rock_row]
        map_row = rock_top_left_y + rock_row
        if right_edge + 1 >= len(map[0]) or map[map_row][right_edge + 1] == '#':
            return False

    for rock_row in range(len(rock) - 1, -1, -1):
        for rock_col in range(len(rock[0]) - 1, -1, -1):
            cur_symbol = rock[rock_row][rock_col]
            if cur_symbol is not None:
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col + 1] = cur_symbol
            if map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] == '@':
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] = '.'

    rock_top_left_x += 1
    return True

def clear_empty_rows():
    global rock_top_left_y
    while '#' not in map[0] and '@' not in map[0]:
        map.pop(0)
        rock_top_left_y -= 1

def move_rock_down():
    global rock_top_left_y
    rock = get_current_rock_shape()
    bottom_boundaries = rock_bottom_boundaries[current_rock % len(rocks)]

    for rock_col in range(0, len(rock[0])):
        bottom_edge = rock_top_left_y + bottom_boundaries[rock_col]
        map_col = rock_top_left_x + rock_col
        if bottom_edge + 1 >= len(map) or map[bottom_edge + 1][map_col] == '#':
            return False

    for rock_row in range(len(rock) - 1, -1, -1):
        for rock_col in range(0, len(rock[0])):
            cur_symbol = rock[rock_row][rock_col]
            if cur_symbol is not None:
                map[rock_top_left_y + rock_row + 1][rock_top_left_x + rock_col] = cur_symbol
            if map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] == '@':
                map[rock_top_left_y + rock_row][rock_top_left_x + rock_col] = '.'

    rock_top_left_y += 1
    clear_empty_rows()

    return True

def fire_jet():
    global current_iteration
    direction_sym = directions[current_iteration % len(directions)]
    if direction_sym == '<':
        move_rock_left()
    elif direction_sym == '>':
        move_rock_right()

    current_iteration += 1

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue
    directions = directions + list(line)

insert_rock()
max_rocks = 2022
while current_rock < max_rocks:
    fire_jet()
    could_move_down = move_rock_down()
    if not could_move_down:
        solidify_rock()
        if current_rock != max_rocks:
            insert_rock()
visualize(True)

print(len(map))