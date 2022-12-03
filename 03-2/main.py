badge_total = 0
groups = []

def priority(char):
    ascii = ord(char)
    if ascii > 96:
        return ascii - 96
    return ascii - 64 + 26

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    stripped_line = line.strip()
    if stripped_line == "":
        continue

    if len(groups) == 0 or len(groups[-1]) == 3:
        groups.append([stripped_line])
    else:
        groups[-1].append(stripped_line)

for group in groups:
    for item in group[0]:
        if group[1].find(item) != -1 and group[2].find(item) != -1:
            badge_total += priority(item)
            break

print(badge_total)
