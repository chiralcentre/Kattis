from sys import stdin,stdout
from math import ceil

N = int(stdin.readline())
counts = [0 for _ in range(10001)]
responses = list(map(int,stdin.readline().split()))
for c in responses:
    counts[c] += 1
minimum = sum(ceil(counts[i]/(i+1))*(i+1) for i in range(1,10001))
stdout.write(str(minimum))
