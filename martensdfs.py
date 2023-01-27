from sys import stdin,stdout

def solve(adjSet,order,N):
    if len(order) != N: return "NO" #graph is connected
    visited = [False for _ in range(N)]
    prev = []
    for i in range(N - 1):
        if order[i + 1] not in adjSet[order[i]]:
            for v in adjSet[order[i]]: #must visit all neighbours first
                if not visited[v]:
                    return "NO"
            while prev and order[i + 1] not in adjSet[prev[-1]]:
                prev.pop()
            if not prev: return "NO"
        prev.append(order[i])
        visited[order[i]] = True
    return "YES"
        
    
N,E = map(int,stdin.readline().split())
adjSet = [set() for _ in range(N)]
for i in range(E):
    a,b = map(int,stdin.readline().split())
    adjSet[a].add(b); adjSet[b].add(a)
order = list(map(int,stdin.readline().split()))
stdout.write(solve(adjSet,order,N))
