import os
import re
from pprint import pprint

class Valve(object):
    def __init__(self, name, flow_rate, neighbors):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = neighbors if neighbors else set()
        self.open = False
        self.weights = {}

    def __str__(self):
        return f'Valve {self.name} with flow rate {self.flow_rate} and neighbors {self.neighbors}'

    def __repr__(self):
        return self.__str__()

valves = {}

# def traverse(node, visited, minutes_remaining, indent):

#     print(f'{indent}Visiting node {node.name} with {minutes_remaining} minutes left. Neighbors: {node.neighbors}')

#     if minutes_remaining <= 0:
#         print(f'{indent}No time left.')
#         return [None, 0, minutes_remaining, False]

#     visited.add(node)

#     immediate_gain = 0
#     if node.flow_rate != 0:
#         immediate_gain = (minutes_remaining - 1) * node.flow_rate

#     paths_after_opening = {}
#     paths_before_opening = {}

#     neighbors = set([valves[neighbor_node] for neighbor_node in node.neighbors])
#     if not neighbors.difference(visited):
#         print(f'{indent}No neighbors, so returning my own value.')
#         return [None, immediate_gain, minutes_remaining - 1, True]

#     for neighbor in neighbors:
#         if not node.open:
#             paths_after_opening[neighbor.name] = traverse(neighbor, visited.copy(), minutes_remaining - 2, indent + '  ')
#         paths_before_opening[neighbor.name] = traverse(neighbor, visited.copy(), minutes_remaining - 1, indent + '  ')

#     max_path_after_opening = None
#     max_path_before_opening = None
#     max_path_before_opening_value = 0
#     max_path_after_opening_value = 0
#     for valve_name, path in paths_after_opening.items():
#         if path[1] + immediate_gain > max_path_after_opening_value:
#             max_path_after_opening = valve_name
#             max_path_after_opening_value = path[1] + immediate_gain

#     for valve_name, path in paths_before_opening.items():
#         after_gain = (path[2] - 1) * node.flow_rate
#         if path[1] + after_gain > max_path_before_opening_value:
#             max_path_before_opening = valve_name
#             max_path_before_opening_value = path[1] + after_gain

#     print(f'{indent}Before scores: {[(name, arr[1]) for name, arr in paths_before_opening.items()]}')
#     print(f'{indent}After scores: {[(name, arr[1]) for name, arr in paths_after_opening.items()]}')

#     should_open_first = max_path_after_opening_value > max_path_before_opening_value + immediate_gain
#     if should_open_first:
#         print(f'{indent}Should open first. Value: {max_path_after_opening_value}')
#         return [max_path_after_opening, max_path_after_opening_value, minutes_remaining - 1, True]
#     else:
#         print(f'{indent}Should traverse further before opening. Value: {max_path_before_opening_value}')
#         return [max_path_before_opening, max_path_before_opening_value, minutes_remaining - 1, False]

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    matches = re.match(r'Valve ([^\s]+) has flow rate=(\d+); tunnels? leads? to valves? (.*)', line)
    name = matches.group(1)
    flow_rate = int(matches.group(2))
    neighbors = set(matches.group(3).split(', '))
    valves[name] = Valve(name, flow_rate, neighbors)

# result = traverse(valves['AA'], set(), 30, '')
# print(result)