import os
import re

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "input.txt")) as f:
    lines = f.readlines()

packets = [[[2]], [[6]]]

def parse_list(input):
    packet = []
    input = input[1:len(input) - 1]

    while input:
        numeric_match = re.match(r'\d+', input)
        slide_input = 0
        if numeric_match is not None:
            number = numeric_match.group(0)
            packet.append(int(number))
            slide_input = len(number) + 1
        else:
            brace_level = 1
            end_marker = 0
            for i in range(1, len(input)):
                if input[i] == '[':
                    brace_level += 1
                elif input[i] == ']':
                    brace_level -= 1
                if brace_level == 0:
                    end_marker = i
                    break
            packet.append(parse_list(input[:i + 1]))
            slide_input = end_marker + 2

        if slide_input <= len(input):
            input = input[slide_input:]
        else:
            input = ""

    return packet

def lists_match(list1, list2):
    for i in range(0, max(len(list1), len(list2))):
        if i >= len(list1):
            return True

        if i >= len(list2):
            return False

        left = list1[i]
        right = list2[i]
        if type(left) == list and type(right) == int:
            right = [right]
        elif type(left) == int and type(right) == list:
            left = [left]

        if type(left) == list:
            match = lists_match(left, right)
            if not match:
                return False
            elif left != right:
                return True
        else:
            if left < right:
                return True
            elif left > right:
                return False

    return True

def merge(left, right):
    result = []
    while left and right:
        if lists_match(left[0], right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result

def merge_sort(packets):
    if len(packets) <= 1:
        return packets

    left = []
    right = []
    for i in range(0, len(packets)):
        if i < int(len(packets) / 2):
            left.append(packets[i])
        else:
            right.append(packets[i])

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

for i in range(0, len(lines)):
    line = lines[i].strip()
    if line == '':
        continue

    packets.append(parse_list(line))

sorted = merge_sort(packets)

decoder_key = 1
packet_index = 1
for packet in sorted:
    if packet == [[2]] or packet == [[6]]:
        decoder_key *= packet_index
    packet_index += 1

print(decoder_key)