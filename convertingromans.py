from sys import stdin,stdout

mappings = {"I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000}

for _ in range(int(stdin.readline())):
    line = stdin.readline().strip()
    #best[i] stores the largest digit from index i to end of array
    best = [-1 for i in range(len(line))]
    highest = -1
    for i in range(len(line) - 1, -1,-1):
        highest = max(highest, mappings[line[i]])
        best[i] = highest
    total = 0
    for i in range(len(line)):
        curr = mappings[line[i]]
        total += curr if curr >= best[i] else -curr
    stdout.write(f"{total}\n")
