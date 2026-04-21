from sys import stdin

N = int(stdin.readline())
prices = list(map(int,stdin.readline().split()))
# try every possible interval, runs in O(N log N) time
best = pow(10,18)
for i in range(1,N + 1):
    cost = 0
    for j in range(0,N,i):
        cost += prices[j] * min(i,N - j)
    best = min(cost,best)
print(best)
