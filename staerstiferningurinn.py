from sys import stdin

A,S = 0,0
for _ in range(int(stdin.readline())):
    a,b = map(int,stdin.readline().split())
    if a == b and (W := a * b) > A:
        A,S = W,a
print(f"{S} {S}")
