from sys import stdin,stdout
from collections import deque

for _ in range(int(stdin.readline())):
    N = int(stdin.readline())
    scores = deque(sorted(map(int,stdin.readline().split())))
    S = 0
    while scores:
        scores.popleft(); scores.pop()
        S += scores.pop()
    stdout.write(f"{S}\n")
