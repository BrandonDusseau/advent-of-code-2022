from pprint import pprint

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

scores = []
for row in range(0, len(rows)):
    for col in range(0, len(cols)):
        height = rows[row][col]
        up_view = 0
        for i in reversed(range(0, row)):
            up_view += 1
            if cols[col][i] >= height:
                break

        down_view = 0
        for i in range(row + 1, len(cols)):
            down_view += 1
            if cols[col][i] >= height:
                break

        left_view = 0
        for i in reversed(range(0, col)):
            left_view += 1
            if rows[row][i] >= height:
                break

        right_view = 0
        for i in range(col + 1, len(rows)):
            right_view += 1
            if rows[row][i] >= height:
                break

        scores.append(up_view * down_view * right_view * left_view)

print(max(scores))
