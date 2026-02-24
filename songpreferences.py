from sys import stdin,stdout

n = int(stdin.readline())
original = list(map(int,stdin.readline().split()))
pos = {}
for i in range(n):
    pos[original[i]] = i
for _ in range(int(stdin.readline())):
    perm = list(map(int,stdin.readline().split()))
    new_pos = {}
    for i in range(n):
        new_pos[perm[i]] = i
    ans = 0
    for i in range(1,n + 1):
        for j in range(i + 1, n + 1):
            d1,d2 = pos[i] - pos[j],new_pos[i] - new_pos[j]
            if d1 * d2 < 0:
                ans += 1
    stdout.write(f"{ans}\n")
