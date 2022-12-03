with open("input.txt") as f:
    lines = f.readlines()

elf_totals = [0]
index = 0

for line in lines:
    stripped_line = line.strip()
    if stripped_line == "":
        index += 1
        elf_totals.append(0)
        continue
    elf_totals[index] += int(stripped_line)

top_three = [0, 0, 0]
for elf in elf_totals:
    if elf > top_three[0]:
        top_three[2] = top_three[1]
        top_three[1] = top_three[0]
        top_three[0] = elf
    elif elf > top_three[1]:
        top_three[2] = top_three[1]
        top_three[1] = elf
    elif elf > top_three[2]:
        top_three[2] = elf

print(str(sum(top_three)))
