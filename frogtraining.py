from sys import stdin,setrecursionlimit
from functools import lru_cache

setrecursionlimit(100000)

@lru_cache(None)
def solve(r,idx):
    global heights
    if r == 0:
        return 1
    if r < 0:
        return 0
    if idx == len(heights):
        return 0
    # use current jump height again
    take = solve(r - heights[idx],idx)
    skip = solve(r,idx + 1)
    return take + skip
        
heights = list(map(int,stdin.readline().split()))
h = int(stdin.readline())
print(solve(h,0))
