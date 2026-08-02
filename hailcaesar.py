def detect_shift(line):
    return ord("H") - ord(line[0])

first = input().strip("\n")
shift = detect_shift(first)
print("Hail, Caesar!")
for _ in range(3):
    line = input().strip("\n")
    output = []
    for char in line:
        x = ord(char) - 32
        x = (x + shift) % 95 # wrap around
        output.append(chr(x + 32))
    print("".join(output))
