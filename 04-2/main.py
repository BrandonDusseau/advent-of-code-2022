overlaps = 0

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

    found_overlap = False
    for elf2zone in elf2range:
        if elf2zone in elf1range:
            found_overlap = True
            break

    if not found_overlap:
        for elf1zone in elf1range:
            if elf1zone in elf2range:
                found_overlap = True
                break

    if found_overlap:
        overlaps += 1

print(str(overlaps))
