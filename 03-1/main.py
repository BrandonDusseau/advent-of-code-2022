total_incorrect = 0

def priority(char):
    ascii = ord(char)
    if ascii > 96:
        return ascii - 96
    return ascii - 64 + 26

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    stripped_line = line.strip()
    if (stripped_line == ""):
        continue

    compartment1 = stripped_line[:int(len(stripped_line) / 2)]
    compartment2 = stripped_line[int(len(stripped_line) / 2):]

    done = False
    for i in compartment1:
        if done:
            break
        for j in compartment2:
            if done:
                break
            elif (i == j):
                total_incorrect += priority(i)
                done = True

print(total_incorrect)
