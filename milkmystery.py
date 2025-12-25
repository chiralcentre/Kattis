from sys import stdin

N, K = map(int, stdin.readline().split())
bowls = list(map(int, stdin.readline().split()))

current = sum(bowls[:K])
ans = current
for i in range(K, N):
    current += bowls[i]
    current -= bowls[i - K]
    ans = max(ans, current)
print(ans)
