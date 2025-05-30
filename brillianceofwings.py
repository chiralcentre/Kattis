from sys import stdin

N = int(stdin.readline())
first_edges = set()
for i in range(N - 1):
    u,v = map(int,stdin.readline().split())
    u,v = sorted([u,v])
    first_edges.add(u * N + v)
ans = 0
for i in range(N - 1):
    u,v = map(int,stdin.readline().split())
    u,v = sorted([u,v])
    if u * N + v not in first_edges:
        ans += 1
print(ans)
