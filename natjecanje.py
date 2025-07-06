from sys import stdin

N,S,R = map(int,stdin.readline().split())
damaged = sorted(map(int,stdin.readline().split()))
reserve = set(map(int,stdin.readline().split()))
cannot_start = 0
for d in damaged:
    lower = d - 1
    if lower in reserve:
        reserve.discard(lower)
        continue
    upper = d + 1
    if upper in reserve:
        reserve.discard(upper)
        continue
    cannot_start += 1
print(cannot_start)
    
