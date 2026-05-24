from sys import stdin

def parse_time(s):
    h,m,sec = map(int,s.split(":"))
    return h * 3600 + m * 60 + sec

n,total = stdin.readline().split()
n,total = int(n),parse_time(total)
tasks = []
for _ in range(n):
    t,v = stdin.readline().split()
    t,v = parse_time(t),int(v)
    tasks.append((t,v))
# 0/1 knapsack, capacity raised by 1 min to accommodate switching cost
cap = total + 60
dp = [0] * (cap + 60)
for t, v in tasks:
    cost = t + 60  # include switching cost
    for c in range(cap, cost - 1, -1):
        dp[c] = max(dp[c], dp[c - cost] + v)
print(max(dp))
