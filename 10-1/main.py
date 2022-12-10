with open("input.txt") as f:
    lines = f.readlines()

register_x = 1
cycle = 0
signal_history = []

def check_signal():
    if cycle == 20 or (cycle - 20) % 40 == 0:
        signal_history.append(register_x * cycle)

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    command = line.split()

    if command[0] == 'noop':
        cycle += 1
        check_signal()
    elif command[0] == 'addx':
        cycle += 1
        check_signal()
        cycle += 1
        check_signal()
        register_x += int(command[1])

print(sum(signal_history))
