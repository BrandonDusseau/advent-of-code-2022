import os
import re

class Sensor(object):
    def __init__(self, x, y, beacon_x, beacon_y):
        self.x = x
        self.y = y
        self.beacon_x = beacon_x
        self.beacon_y = beacon_y

    def beacon_distance(self):
        x_diff = abs(self.x - self.beacon_x)
        y_diff = abs(self.y - self.beacon_y)
        return x_diff + y_diff

    def point_in_range(self, x, y):
        max_distance = self.beacon_distance()
        return abs(self.x - x) + abs(self.y - y) <= max_distance

    def __str__(self):
        return self.__repr__();

    def __repr__(self):
        return f'{self.x}, {self.y} with beacon distance {self.beacon_distance()}'

def ranges_overlap(range_1, range_2):
    return not (range_1[1] < range_2[0] or range_2[1] < range_1[0])

sensors = []
search_upper_bound = 4000000

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue
    matches = re.match(r'Sensor at x=([-0-9]+), y=([-0-9]+): closest beacon is at x=([-0-9]+), y=([-0-9]+)', line)
    sensor_x = int(matches.group(1))
    sensor_y = int(matches.group(2))
    beacon_x = int(matches.group(3))
    beacon_y = int(matches.group(4))

    sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))

found_x = None
found_y = None
for y in range(0, search_upper_bound + 1):
    if y % 100000 == 0:
        print(f"Checking row {y}")

    sensors_in_range = [i for i in sensors if abs(y - i.y) <= i.beacon_distance()]
    x_bounds = []
    for sensor in sensors_in_range:
        row_distance_from_origin = abs(sensor.y - y)
        available_x = sensor.beacon_distance() - row_distance_from_origin
        x_bounds.append([max(0, sensor.x - available_x), min(search_upper_bound + 1, sensor.x + available_x)])

    combined_bounds = x_bounds.copy()
    no_action_possible = False

    while len(combined_bounds) != 1 and not no_action_possible:
        for i in range(0, len(combined_bounds)):
            range_1 = combined_bounds[i]
            found_overlap = False
            for j in range(i + 1, len(combined_bounds)):
                range_2 = combined_bounds[j]
                if ranges_overlap(range_1, range_2):
                    new_range = [min(range_1[0], range_2[0]), max(range_1[1], range_2[1])]
                    combined_bounds = [new_range] + [combined_bounds[k] for k in range(0, len(combined_bounds)) if k != i and k != j]
                    found_overlap = True
                    break

            if found_overlap:
                break
            elif i == len(combined_bounds) - 1:
                no_action_possible = True

    if len(combined_bounds) != 1:
        found_y = y

        min_upper_bound = float('inf')
        for bound in combined_bounds:
            if bound[1] < min_upper_bound:
                min_upper_bound = bound[1]
        found_x = min_upper_bound + 1
        break

print((found_x, found_y))
print(found_x * 4000000 + found_y)