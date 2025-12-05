from sys import stdin,stdout
from bisect import bisect_left

# runs in O(m log n)
n,m = map(int,stdin.readline().split())
good = [int(stdin.readline()) for _ in range(n)]
for _ in range(m):
    f = int(stdin.readline())
    index = bisect_left(good,f)
    if index == 0:
        stdout.write(f"{good[0] - f}\n")
    elif index == n:
        stdout.write(f"{good[-1] - f}\n")
    else:
        L = f - good[index - 1]
        R = good[index] - f
        if L < R:
            stdout.write(f"{-L}\n")
        else:
            stdout.write(f"{R}\n")
