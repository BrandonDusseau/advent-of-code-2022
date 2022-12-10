with open("input.txt") as f:
    lines = f.readlines()

register_x = 1
cycle = 0

crt = [['.' for _ in range(0, 40)] for _ in range(0, 6)]

def display_crt():
    for row in range(0, len(crt)):
        print(''.join(crt[row]))

def update_crt():
    pixel_row = int(cycle / 40)
    pixel_col = (cycle % 40) - 1
    sprite_min = register_x - 1
    sprite_max = register_x + 1

    if pixel_col >= sprite_min and pixel_col <= sprite_max:
        crt[pixel_row][pixel_col] = '#'

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    command = line.split()

    if command[0] == 'noop':
        cycle += 1
        update_crt()
    elif command[0] == 'addx':
        cycle += 1
        update_crt()
        cycle += 1
        update_crt()
        register_x += int(command[1])

display_crt()
