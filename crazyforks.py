from sys import stdin

def count_black_pixels(line):
    return sum(char == "#" for char in line)

tines = [0 for _ in range(100)]
tine_begin = False
handle_length = 0
for line in stdin:
    line = line.rstrip()
    if not tine_begin:
        black_pixels = count_black_pixels(line)
        if black_pixels == len(line) and black_pixels >= 3:
            tine_begin = True
        else:
            handle_length += 1
    else:
        for i in range(len(line)):
            if line[i] == "#":
                tines[i] += 1
lengths = [num for num in tines if num > 0]
print(handle_length)
print(" ".join(str(num) for num in lengths))
