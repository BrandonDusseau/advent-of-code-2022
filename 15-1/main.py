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

    def add_locations_in_range(self):
        global locations_without_beacons
        global min_x
        global max_x
        max_distance = self.beacon_distance()
        y_lower = self.y - max_distance
        y_upper = self.y + max_distance
        if target_y in range(y_lower, y_upper + 1):
            row = target_y
            row_distance_from_origin = abs(self.y - row)
            available_x = max_distance - row_distance_from_origin
            for col in range(self.x - available_x, self.x + available_x + 1):
                if col < min_x:
                    min_x = col
                if col > max_x:
                    max_x = col
                locations_without_beacons.add((col, row))

    def __repr__(self):
        return f'Sensor {self.x}, {self.y} with beacon distance {self.beacon_distance()}'

sensors = []
min_x = float('inf')
max_x = 0
min_y = float('inf')
max_y = 0
target_y = 2000000
locations_without_beacons = set()

def visualize():
    count_row_0 = [' ', ' ', ' ']
    count_row_1 = [' ', ' ', ' ']
    for col in range(min_x, max_x + 1):
        if col % 5 == 0 and col >= 10:
            count_row_0.append(str(int(col / 10)))
        else:
            count_row_0.append(' ')

        if col % 5 == 0:
            count_row_1.append(str(col % 10))
        else:
            count_row_1.append(' ')

    print(''.join(count_row_0))
    print(''.join(count_row_1))
    for row in range(min_y, max_y + 1):
        row_array = []
        for col in range(min_x, max_x + 1):
            symbol = '.'
            if (col, row) in locations_without_beacons:
                symbol = '#'
            for sensor in sensors:
                if sensor.x == col and sensor.y == row:
                    symbol = 'S'
                    break
                if sensor.beacon_x == col and sensor.beacon_y == row:
                    symbol = 'B'
                    break
            row_array.append(symbol)
        print(str(row).rjust(len(str(max_y)) + 1, ' ') + ' ' + ''.join(row_array))
    print()

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

    if sensor_x < min_x:
        min_x = sensor_x
    if sensor_x > max_x:
        max_x = sensor_x
    if sensor_y < min_y:
        min_y = sensor_y
    if sensor_y > max_y:
        max_y = sensor_y
    if beacon_x < min_x:
        min_x = beacon_x
    if beacon_x > max_x:
        max_x = beacon_x
    if beacon_y < min_y:
        min_y = beacon_y
    if beacon_y > max_y:
        max_y = beacon_y

    sensors.append(Sensor(sensor_x, sensor_y, beacon_x, beacon_y))

for sensor in sensors:
    sensor.add_locations_in_range()

for sensor in sensors:
    key = (sensor.beacon_x, sensor.beacon_y)
    if key in locations_without_beacons:
        locations_without_beacons.remove(key)

in_range = 0
for x in range(min_x, max_x):
    if (x, target_y) in locations_without_beacons:
        in_range += 1

print(in_range)