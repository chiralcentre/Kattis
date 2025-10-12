from sys import stdin

INF = pow(10,9)
n,c = map(int,stdin.readline().split())
meetings = [INF for _ in range(24)]
for i in range(n):
    t,p = map(int,stdin.readline().split())
    if p <= c:
        meetings[t] = min(p, meetings[t])
eligible = sorted([x for x in meetings if x != INF])
ans,total = 0,0
for p in eligible:
    if total + p <= c:
        total += p
        ans += 1
    else:
        break
print(ans)
