from sys import stdin

def solve():
    n,c,s,f = map(int,stdin.readline().split())
    s -= 1 # offset by 1 due to zero indexing
    stdin.readline()
    final = set(map(lambda x: int(x) - 1, stdin.readline().split()))
    adjMat = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n)]
    # perform DFS to check if final states are reachable from start state in O(n + n * c)
    visited = [False for _ in range(n)]; visited[s] = True
    frontier = [s]
    while frontier:
        u = frontier.pop()
        for v in adjMat[u]:
            if not visited[v]:
                if v in final:
                    return "non-empty"
                frontier.append(v)
                visited[v] = True
    return "empty"   
    
print(solve())
