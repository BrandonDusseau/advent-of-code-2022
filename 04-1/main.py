
full_overlaps = 0

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    stripped_line = line.strip()
    if stripped_line == "":
        continue

    (elf1, elf2) = stripped_line.split(',')
    (elf1lower, elf1upper) = elf1.split('-')
    (elf2lower, elf2upper) = elf2.split('-')
    elf1range = range(int(elf1lower), int(elf1upper) + 1)
    elf2range = range(int(elf2lower), int(elf2upper) + 1)

    elf2mismatch = False
    for elf2zone in elf2range:
        if elf2zone not in elf1range:
            elf2mismatch = True
            break
    if not elf2mismatch:
        full_overlaps += 1
        continue

    elf1mismatch = False
    for elf1zone in elf1range:
        if elf1zone not in elf2range:
            elf1mismatch = True
            break
    if not elf1mismatch:
        full_overlaps += 1

print(str(full_overlaps))
