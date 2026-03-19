from sys import stdin

n,m = map(int,stdin.readline().split())
investments,curr = [],m
for _ in range(n):
    c,r = map(int,stdin.readline().split())
    if r > c:
        investments.append((c,r))
# sort in ascending order of cost, break ties in descending order of revenue
investments.sort(key = lambda x: (x[0],-x[1]))
for c,r in investments:
    if c > curr:
        break
    else:
        curr += r - c
print(curr - m)
