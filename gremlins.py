from sys import stdin,stdout

n,m = map(int,stdin.readline().split())
original = [stdin.readline().strip() for _ in range(n)]
indices = {}
for i in range(m):
    item = stdin.readline().strip()
    indices[item] = i + 1
for i in range(n):
    item = original[i]
    if item not in indices:
        stdout.write("stolen!\n")
    else:
        stdout.write(f"{indices[item]}\n")
