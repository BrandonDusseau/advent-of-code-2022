import math
import re

class Monkey(object):
    def __init__(self, id):
        self.id = id
        self.item_ids = []
        self.operator = None
        self.operand = None
        self.divisor = None
        self.true_target = None
        self.false_target = None
        self.inspections = 0

    def __str__(self):
        return (f'Monkey {self.id}\n' +
            '  Items: ' + ', '.join(map(str, self.item_ids)) + '\n' +
            f'  Inspections: {self.inspections}\n' +
            f'  Operator: {self.operator}\n' +
            f'  Operand: {self.operand}\n' +
            f'  Divisor: {self.divisor}\n' +
            f'  True target: {self.true_target}\n' +
            f'  False target: {self.false_target}\n')

monkeys = []
all_items = []

with open("input.txt") as f:
    lines = f.readlines()

# Parse input
monkey_id = -1
all_items_index = 0
for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    if line.startswith('Monkey'):
        monkey_id += 1
        monkeys.append(Monkey(monkey_id))
        continue
    elif line.startswith('Starting items:'):
        items = [int(x) for x in re.findall(r'\d+', line)]
        for item in items:
            all_items.append(item)
            monkeys[monkey_id].item_ids.append(len(all_items) - 1)
        continue
    elif line.startswith('Operation:'):
        result = re.search(r'new = old (.) (.+)', line)
        monkeys[monkey_id].operator = result.groups()[0]
        monkeys[monkey_id].operand = result.groups()[1]
        continue
    elif line.startswith('Test:'):
        monkeys[monkey_id].divisor = int(re.findall(r'(\d+)', line)[0])
        continue
    elif 'true' in line:
        monkeys[monkey_id].true_target = int(re.findall(r'(\d+)', line)[0])
        continue
    elif 'false' in line:
        monkeys[monkey_id].false_target = int(re.findall(r'(\d+)', line)[0])
        continue

lcm = math.lcm(*[monkey.divisor for monkey in monkeys])

for i in range(1, 10001):
    for monkey in monkeys:
        while monkey.item_ids:
            item_id = monkey.item_ids.pop(0)
            worry_level = all_items[item_id]
            monkey.inspections += 1
            operand = worry_level if monkey.operand == 'old' else int(monkey.operand)

            if monkey.operator == '*':
                worry_level *= operand
            elif monkey.operator == '+':
                worry_level += operand

            if worry_level % monkey.divisor == 0:
                monkeys[monkey.true_target].item_ids.append(item_id)
            else:
                monkeys[monkey.false_target].item_ids.append(item_id)

            all_items[item_id] = worry_level % lcm

    if i % 1000 == 0 or i == 20 or i == 1:
        print(f'== After round {i} ==')
        for monkey in monkeys:
            print(f'Monkey {monkey.id} inspected items {monkey.inspections} times')
        print()

most_active = Monkey(-1)
second_most_active = Monkey(-1)
for monkey in monkeys:
    if monkey.inspections > most_active.inspections:
        second_most_active = most_active
        most_active = monkey
    elif monkey.inspections > second_most_active.inspections:
        second_most_active = monkey

monkey_business = most_active.inspections * second_most_active.inspections

print(monkey_business)