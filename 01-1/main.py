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

print(str(max(elf_totals)))