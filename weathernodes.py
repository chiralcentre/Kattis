from sys import stdin

N = int(stdin.readline())
if N == 0:
    print(0)
else:
    values = [float(stdin.readline()) for _ in range(N)]
    average = sum(values) / N
    print(sum(1 for v in values if abs(v - average) > 10))
