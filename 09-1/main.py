with open("input.txt") as f:
    lines = f.readlines()

seen_positions = {(0,0)}
head_x = 0
head_y = 0
tail_x = 0
tail_y = 0

def head_in_range():
    if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        return False
    return True

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    (direction, num_spaces) = line.split()
    num_spaces = int(num_spaces)
    print(f'Head moving {num_spaces} steps {direction}')

    # This is technically incorrect, but works. I misinterpreted the rules.
    if direction == 'R':
        for i in range(head_x + 1, head_x + num_spaces + 1):
            head_x = i
            if head_in_range():
                continue
            tail_x = i - 1
            tail_y = head_y
            seen_positions.add((tail_x, tail_y))
            print(f'Tail now at {tail_x},{tail_y}')
    elif direction == 'L':
        for i in range(head_x - 1, head_x - num_spaces - 1, -1):
            head_x = i
            if head_in_range():
                continue
            tail_x = i + 1
            tail_y = head_y
            seen_positions.add((tail_x, tail_y))
            print(f'Tail now at {tail_x},{tail_y}')
    elif direction == 'U':
        for i in range(head_y + 1, head_y + num_spaces + 1):
            head_y = i
            if head_in_range():
                continue
            tail_x = head_x
            tail_y = i - 1
            seen_positions.add((tail_x, tail_y))
            print(f'Tail now at {tail_x},{tail_y}')
    elif direction == 'D':
        for i in range(head_y - 1, head_y - num_spaces - 1, -1):
            head_y = i
            if head_in_range():
                continue
            tail_x = head_x
            tail_y = i + 1
            seen_positions.add((tail_x, tail_y))
            print(f'Tail now at {tail_x},{tail_y}')

    print(f'-- Head now at {head_x},{head_y}')

print(len(seen_positions))
