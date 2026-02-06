from sys import stdin

N = int(stdin.readline())
melons = sorted([int(stdin.readline()) for _ in range(N)])
k = int(stdin.readline())
M = N // k * k
print(sum(melons[i] for i in range(N - M, N,)))
