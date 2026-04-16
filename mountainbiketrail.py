from sys import stdin

# maximum number of groups = N
N = int(stdin.readline())
groupings = {}
for _ in range(N):
    line = stdin.readline().split()
    m = 0 if line[0] == "just" else int(line[0])
    if m + 1 in groupings:
        if groupings[m + 1] == 1:
            groupings.pop(m + 1)
        else:
            groupings[m + 1] -= 1
    groupings[m] = groupings.get(m,0) + 1
L = sum(value for key,value in groupings.items())
print(f"{L} {N}")
