from sys import stdin

def transform(time_string):
    h,m,s = map(int,time_string.split(":"))
    return h * 3600 + m * 60 + s

n,m = map(int,stdin.readline().split())
arrivals = [transform(stdin.readline().strip()) for _ in range(n)]
departures = [transform(stdin.readline().strip()) for _ in range(m)]
s = int(stdin.readline())
best = -1
for i in range(n):
    for j in range(m):
        a,d = arrivals[i],departures[j]
        t = d - a
        if t >= s:           
            best = t if best == -1 else min(best,t)
print(best)
