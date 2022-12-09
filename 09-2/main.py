class Knot(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.seen_positions = set((0,0))

    def move(self, x, y):
        self.x = x
        self.y = y
        self.seen_positions.add((x, y))

with open("input.txt") as f:
    lines = f.readlines()

knots = [Knot() for _ in range(10)]
moves = []

def visualize():
    max_x = 0
    max_y = 0
    min_x = 0
    min_y = 0
    x = 0
    y = 0
    for move in moves:
        (direction, num_spaces) = move
        if direction == 'R':
            x += num_spaces
        elif direction == 'L':
            x -= num_spaces
        elif direction == 'U':
            y += num_spaces
        elif direction == 'D':
            y -= num_spaces

        if x > max_x:
            max_x = x
        if x < min_x:
            min_x = x
        if y > max_y:
            max_y = y
        if y < min_y:
            min_y = y

    width = max_x - min_x + 1
    height = max_y - min_y + 1
    origin_x = -min_x
    origin_y = max_y

    grid = []
    for _ in range(0, height):
        grid.append(['.' for _ in range(0, width)])

    for row in range(0, len(grid)):
        for col in range(0, len(grid[0])):
            grid_x = -origin_x + col
            grid_y = origin_y - row
            for i in reversed(range(0, len(knots))):
                knot = knots[i]
                if knot.x == grid_x and knot.y == grid_y:
                    grid[row][col] = str(i) if i != 0 else 'H'

    for row in range(0, len(grid)):
        print(''.join(grid[row]))
    print()

def last_knot_in_range(index):
    if abs(knots[index - 1].x - knots[index].x) > 1 or abs(knots[index - 1].y - knots[index].y) > 1:
        return False
    return True

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue
    (direction, num_spaces) = line.split()
    moves.append((direction, int(num_spaces)))

print("== Initial State ==\n")
visualize()

for move in moves:
    (direction, num_spaces) = move
    print(f"== {direction} {num_spaces} ==\n")

    head_positions = []
    if direction == 'R':
        head_positions = [(x, knots[0].y) for x in range(knots[0].x + 1, knots[0].x + num_spaces + 1)]
    elif direction == 'L':
        head_positions = [(x, knots[0].y) for x in range(knots[0].x - 1, knots[0].x - num_spaces - 1, -1)]
    elif direction == 'U':
        head_positions = [(knots[0].x, y) for y in range(knots[0].y + 1, knots[0].y + num_spaces + 1)]
    elif direction == 'D':
        head_positions = [(knots[0].x, y) for y in range(knots[0].y - 1, knots[0].y - num_spaces - 1, -1)]

    for head_pos in head_positions:
        (head_x, head_y) = head_pos
        knots[0].move(head_x, head_y)

        for index in range(1, len(knots)):
            last_knot = knots[index - 1]
            cur_knot = knots[index]
            if last_knot_in_range(index):
                continue

            need_move_right = last_knot.x > cur_knot.x
            need_move_left = last_knot.x < cur_knot.x
            need_move_up = last_knot.y > cur_knot.y
            need_move_down = last_knot.y < cur_knot.y

            x_shift = 0
            y_shift = 0
            if need_move_right:
                x_shift = 1
            elif need_move_left:
                x_shift = -1
            if need_move_up:
                y_shift = 1
            elif need_move_down:
                y_shift = -1

            knots[index].move(cur_knot.x + x_shift, cur_knot.y + y_shift)

        # visualize()

print(len(knots[9].seen_positions))
