import re

with open("input.txt") as f:
    lines = f.readlines()

stacks = []

# Locate the line that has the stack counts.
stack_line = None
number_stacks = 0
for i in range(0, len(lines)):
    if re.match(r'^\s+\d', lines[i]):
        stack_line = i
        number_stacks = int(re.findall(r'\d+', lines[i])[-1])
        break

for i in range(0, number_stacks):
    stacks.append([])

# Start building the stacks from the bottom.
for i in reversed(range(0, number_stacks)):
    line = lines[i].rstrip()
    stack_num = 0
    position = 1
    while stack_num < number_stacks and position < len(line):
        stack_item = line[position]
        if stack_item != ' ':
            stacks[stack_num].append(stack_item)
        position += 4
        stack_num += 1

# Process move instructions.
instruction_first_line = stack_line + 2
for line in lines[instruction_first_line:]:
    (number_to_move, from_stack, to_stack) = re.search(r'move (\d+) from (\d+) to (\d+)', line).groups()
    number_to_move = int(number_to_move)
    from_stack = int(from_stack) - 1
    to_stack = int(to_stack) - 1

    temp_stack = []
    for i in range(0, number_to_move):
        temp_stack.append(stacks[from_stack].pop())

    temp_stack.reverse()
    stacks[to_stack] = stacks[to_stack] + temp_stack


# Get the top of each stack.
tops = ""
for stack in stacks:
    if len(stack) == 0:
        continue
    tops += stack.pop()

print(tops)
