import os
from hashlib import sha256

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

cache = {}
height_at_cycle = 0
rock_at_cycle = None

def check_cycle():
    global height_at_cycle
    global rock_at_cycle
    rock_tops = [None, None, None, None, None, None, None]
    for row in range(0, len(map)):
        if None not in rock_tops:
            break
        for col in range(0, len(map[0])):
            if rock_tops[col] is None and map[row][col] == '#':
                rock_tops[col] = row

    if None in rock_tops:
        return False

    state_rock = current_rock % len(rocks)
    next_jet = (current_iteration - 1) % len(directions)

    state = [rock_tops, state_rock, next_jet]

    hash = sha256()
    hash.update(repr(state).encode('utf-8'))
    state_hash = hash.hexdigest()

    cycle_found = False
    if state_hash in cache:
        (height_at_cycle, rock_at_cycle) = cache[state_hash]
        cycle_found = True

    cache[state_hash] = (len(map), current_rock)

    return cycle_found

insert_rock()
map_height = 0
cycle_repeats = 0
height_offset = 0
max_rocks = 1000000000000
while current_rock < max_rocks:
    fire_jet()
    could_move_down = move_rock_down()
    if not could_move_down:
        is_cycle = check_cycle()
        map_height = len(map)
        solidify_rock()

        # Math based on https://www.reddit.com/r/adventofcode/comments/znykq2/2022_day_17_solutions/j0lxz9y/
        # because I am too tired to figure it out myself.
        if cycle_repeats == 0 and is_cycle:
            height_now_to_original = map_height - height_at_cycle
            rocks_now_to_original = current_rock - rock_at_cycle
            cycle_repeats = int((max_rocks - current_rock) / rocks_now_to_original)
            height_offset += height_now_to_original * cycle_repeats
            current_rock += rocks_now_to_original * cycle_repeats

        current_rock += 1

        if current_rock != max_rocks:
            insert_rock()

print(len(map) + height_offset)