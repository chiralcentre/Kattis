from sys import stdin,stdout

R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for i in range(R)]
words = []
for i in range(R):
    prev = ""
    for j in range(C):
        if grid[i][j] != "#":
            prev += grid[i][j]
        else:
            if len(prev) >= 2:
                words.append(prev)
            prev = ""
    if len(prev) >= 2:
        words.append(prev)
for i in range(C):
    prev = ""
    for j in range(R):
        if grid[j][i] != "#":
            prev += grid[j][i]
        else:
            if len(prev) >= 2:
                words.append(prev)
            prev = ""
    if len(prev) >= 2:
        words.append(prev)
stdout.write(sorted(words)[0])
