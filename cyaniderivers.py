from sys import stdin

# L represents longest length of contiguous 1s
towers = stdin.readline().strip()
last_seen,L = 0,-1
for i in range(1,len(towers)):
    if towers[i] == "1":
        L = max(L, i - last_seen - 1)
        last_seen = i
print(L // 2 + (L % 2 != 0))
