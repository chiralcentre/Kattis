from sys import stdin

def solve():
    n,p = map(int,stdin.readline().split())
    curr = 0
    for i in range(n):
        c = int(stdin.readline())
        # assume worst case
        # curr = sum of pages stamped thus far
        # note that in the worst case there will be i + 1 divisions after accounting for current trip
        # pigeonhole principle: for trip to be possible, at least one division must be >= c
        if curr + c + i * (c - 1) > p:
            return i
        curr += c
    return n

print(solve())
