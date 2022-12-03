their_rock = "A"
their_paper = "B"
their_scissors = "C"
lose = "X"
draw = "Y"
win = "Z"
my_rock = 0x01
my_paper = 0x02
my_scissors = 0x03

shape_points = {
    my_rock: 1,
    my_paper: 2,
    my_scissors: 3
}
result_points = {
    win: 6,
    draw: 3,
    lose: 0
}

round_points = []

shape_from_result = {
    win: {
        their_rock: my_paper,
        their_paper: my_scissors,
        their_scissors: my_rock
    },
    draw: {
        their_rock: my_rock,
        their_paper: my_paper,
        their_scissors: my_scissors
    },
    lose: {
        their_rock: my_scissors,
        their_paper: my_rock,
        their_scissors: my_paper
    }
}

with open("input.txt") as f:
    lines = f.readlines()

for line in lines:
    stripped_line = line.strip()
    if (stripped_line == ""):
        continue

    (opponent, desired_result) = stripped_line.split()

    my_shape = shape_from_result[desired_result][opponent]
    round_points.append(result_points[desired_result] + shape_points[my_shape])

print(sum(round_points))
