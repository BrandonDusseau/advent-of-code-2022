import re

class Monkey(object):
    def __init__(self, id):
        self.id = id
        self.items = []
        self.operator = None
        self.operand = None
        self.divisor = None
        self.true_target = None
        self.false_target = None
        self.inspections = 0

    def __str__(self):
        return (f'Monkey {self.id}\n' +
            '  Items: ' + ', '.join(map(str, self.items)) + '\n' +
            f'  Inspections: {self.inspections}\n' +
            f'  Operator: {self.operator}\n' +
            f'  Operand: {self.operand}\n' +
            f'  Divisor: {self.divisor}\n' +
            f'  True target: {self.true_target}\n' +
            f'  False target: {self.false_target}\n')

monkeys = []

with open("input.txt") as f:
    lines = f.readlines()

# Parse input
monkey_id = -1
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
        monkeys[monkey_id].items = monkeys[monkey_id].items + items
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

for _ in range(0, 20):
    for monkey in monkeys:
        for item in monkey.items.copy():
            monkey.inspections += 1
            worry_level = item
            operand = worry_level if monkey.operand == 'old' else int(monkey.operand)

            if monkey.operator == '*':
                worry_level *= operand
            elif monkey.operator == '+':
                worry_level += operand
            elif monkey.operator == '-':
                worry_level -= operand
            elif monkey.operator == '/':
                worry_level = int(worry_level / operand)

            worry_level = int(worry_level / 3)

            if worry_level % monkey.divisor == 0:
                monkeys[monkey.true_target].items.append(worry_level)
            else:
                monkeys[monkey.false_target].items.append(worry_level)

            monkey.items.pop(0)

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