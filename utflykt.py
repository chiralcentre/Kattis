from sys import stdin

N = int(stdin.readline())
times = sorted([int(stdin.readline()) for _ in range(N)])
# second bus must be taken at last timing
prefix_sums = [0 for _ in range(N)]
prefix_sums[0] = times[0]
for i in range(1,N):
    prefix_sums[i] = prefix_sums[i - 1]  + times[i]
best = pow(10,20)
# wait time for first bus = times[i] * (i + 1) - prefix_sums[i]
# wait time for second bus = times[-1] * (N - i - 1) - (prefix_sums[-1] - prefix_sums[i])
for i in range(N):
    curr = times[i] * (i + 1) + times[-1] * (N - i - 1) - prefix_sums[-1]
    best = min(best,curr)
print(best)
