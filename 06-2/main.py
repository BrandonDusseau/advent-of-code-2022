with open("input.txt") as f:
    lines = f.readlines()

signal = lines[0].strip()
window_start = 0

marker_found = False
while not marker_found and window_start + 14 < len(signal):
    unique_chars = set(signal[window_start:window_start+14])
    if len(unique_chars) == 14:
        marker_found = True
    else:
        window_start += 1

print(str(window_start + 14))