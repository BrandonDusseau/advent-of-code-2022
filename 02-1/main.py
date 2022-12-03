their_rock = "A"
their_paper = "B"
their_scissors = "C"
my_rock = "X"
my_paper = "Y"
my_scissors = "Z"

shape_points = {
    my_rock: 1,
    my_paper: 2,
    my_scissors: 3
}

round_points = []

def is_win(opponent, me):
    return (opponent == their_rock and me == my_paper) or (opponent == their_paper and me == my_scissors) or (opponent == their_scissors and me == my_rock)

def is_draw(opponent, me):
    return (opponent == their_rock and me == my_rock) or (opponent == their_paper and me == my_paper) or (opponent == their_scissors and me == my_scissors)

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    stripped_line = line.strip()
    if (stripped_line == ""):
        continue

    (opponent, me) = stripped_line.split()

    my_points = 0
    if is_win(opponent, me):
        my_points = 6
    elif is_draw(opponent, me):
        my_points = 3

    my_points += shape_points[me]
    round_points.append(my_points)

print(len(round_points))
print(sum(round_points))
