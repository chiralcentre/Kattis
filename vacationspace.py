from sys import stdin

INF = pow(10,18)
n = int(stdin.readline())
houses = list(map(int,stdin.readline().split()))
if n == 1:
    print(1)
else:
    mappings = {houses[i]: i + 1 for i in range(n)}
    houses = sorted(houses)
    ans,best = 1,-1
    for i in range(n):
        a,b = INF,INF
        if i + 1 < n:
            a = houses[i + 1] - houses[i]
        if i >= 1:
            b = houses[i] - houses[i - 1]
        d = min(a,b)
        if d > best:
            ans,best = mappings[houses[i]],d
        elif d == best and mappings[houses[i]] < ans:
            ans = mappings[houses[i]]
    print(ans)
