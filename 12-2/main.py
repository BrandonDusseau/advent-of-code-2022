import os

class Node(object):
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height
        self.explored = False
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        self.shortest_parent = None

    def reset(self):
        self.shortest_parent = None
        self.explored = False

origin_x = 0
origin_y = 0
destination_x = 0
destination_y = 0

nodes = []
a_nodes = []

def shortest_length_from(start_node):
    for row in range(0, len(nodes)):
        for col in range(0, len(nodes[0])):
            nodes[row][col].reset()

    q = []
    start_node.explored = True
    final_node = None
    q.append(start_node)
    while q:
        current_node = q.pop(0)
        if current_node.x == destination_x and current_node.y == destination_y:
            final_node = current_node
            break
        cur_height = current_node.height

        nodes_to_explore = []
        if current_node.up is not None and current_node.up.height <= cur_height + 1:
            nodes_to_explore.append(current_node.up)
        if current_node.down is not None and current_node.down.height <= cur_height + 1:
            nodes_to_explore.append(current_node.down)
        if current_node.left is not None and current_node.left.height <= cur_height + 1:
            nodes_to_explore.append(current_node.left)
        if current_node.right is not None and current_node.right.height <= cur_height + 1:
            nodes_to_explore.append(current_node.right)

        for adjacent_node in nodes_to_explore:
            if adjacent_node.explored == False:
                adjacent_node.explored = True
                adjacent_node.shortest_parent = current_node
                q.append(adjacent_node)

    if final_node is None:
        return float('inf')

    steps = -1
    current_node = final_node
    while current_node is not None:
        steps += 1
        current_node = current_node.shortest_parent
    return steps

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

for row in range(0, len(lines)):
    line = lines[row].strip()
    if line == '':
        continue

    nodes.append([])

    for col in range(0, len(line)):
        this_node = None
        if line[col] == 'S':
            origin_x = col
            origin_y = row
            this_node = Node(col, row, 1)
        elif line[col] == 'E':
            destination_x = col
            destination_y = row
            this_node = Node(col, row, 26)
        else:
            this_node = Node(col, row, ord(line[col]) - 96)

        if col > 0:
            nodes[row][col - 1].right = this_node
            this_node.left = nodes[row][col - 1]
        if row > 0:
            nodes[row - 1][col].down = this_node
            this_node.up = nodes[row - 1][col]
        nodes[row].append(this_node)

        if this_node.height == 1:
            a_nodes.append(this_node)

node_steps = list(map(shortest_length_from, a_nodes))
print(min(node_steps))
