from sys import stdin

n = int(stdin.readline())
prices = list(map(int,stdin.readline().split()))
ans = 0
for i in range(1,n):
    if prices[i] > prices[i - 1]:
        ans += prices[i] - prices[i - 1]
print(ans)
