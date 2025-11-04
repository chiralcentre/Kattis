from sys import stdin,stdout

# runs in O(N + N / 2 + N /3 + ... + 2) time = O(N log N)
N,T = map(int,stdin.readline().split())
readings = [int(stdin.readline()) for _ in range(N)]
prefix_sums = [readings[0]]
for i in range(1,N):
    prefix_sums.append(prefix_sums[-1] + readings[i])
ans = N // 2 + 1
prev = prefix_sums[0]
d = 0
for i in range(1,N):
    curr = prefix_sums[i] - prefix_sums[i - 1]
    d = max(abs(curr - prev), d)
    prev = curr
if d <= T:
    print(1)
    exit(0)
for j in range(2,N // 2 + 1):
    prev = prefix_sums[j - 1]
    d = 0
    for k in range(j, N - j + 1, j):
        curr = prefix_sums[k + j - 1] - prefix_sums[k - 1]
        diff = abs(curr // j - prev // j)
        d = max(diff,d)
        prev = curr
    if d <= T:
        ans = j
        break
print(ans)
