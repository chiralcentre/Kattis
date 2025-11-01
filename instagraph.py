from sys import stdin

# runs in O(M + N) time
N,M = map(int,stdin.readline().split())
adjSet = [set() for i in range(N)]
transpose = [[] for _ in range(N)] #transpose[u] = [v] -> edge pointing to u from v
for _ in range(M):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    transpose[v].append(u) 
    adjSet[u].add(v)
v,best = -1,-1
for i in range(N):
    CC = 0
    for u in transpose[i]:
        if u not in adjSet[i]:
            CC += 1
    if CC > best:
        v,best = i + 1,CC
print(f"{v} {best}")
