from sys import stdin
from bisect import bisect_left

# code runs in O(n log n) time
n = int(stdin.readline())
stacks = []
for i in range(n):
    _, r = map(int,stdin.readline().split())
    if not stacks:
        stacks.append(r)
    else:
        p = bisect_left(stacks, r)
        if p == len(stacks):
            stacks.append(r)
        else:
            stacks[p] = r
print(len(stacks))
