with open("input.txt") as f:
    lines = f.readlines()

rows = []
cols = []

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    line_split = [int(x) for x in line]
    rows.append(line_split)

    for j in range(0, len(line)):
        if len(cols) < j + 1:
            cols.append([])
        cols[j].append(int(line[j]))

# Edge trees are all visible
visible_trees = (len(rows) * 2) + (len(cols) * 2) - 4

for row in range(1, len(rows) - 1):
    for col in range(1, len(cols) - 1):
        tree = rows[row][col]
        if (max(rows[row][0:col]) < tree or
            max(rows[row][col + 1:len(cols[0])]) < tree or
            max(cols[col][0:row]) < tree or
            max(cols[col][row + 1:len(rows[0])]) < tree):
            visible_trees += 1

print(visible_trees)
