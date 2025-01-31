from sys import stdin
from collections import deque

INF = pow(10,9)
def findShortestLength():
    n,c,s,f = map(int,stdin.readline().split())
    s -= 1 # offset by 1 due to zero indexing
    stdin.readline().strip()
    final = set(map(lambda x: int(x) - 1, stdin.readline().split()))
    # can use set to remove duplicates, cut down on neighbours to enumerate
    adjMat = [list(map(lambda x: int(x) - 1, stdin.readline().split())) for _ in range(n)]
    # perform BFS to find length of shortest word in O(n + n * c)
    d = [INF for _ in range(n)]; d[s] = 0
    frontier = deque([s])
    while frontier:
        u = frontier.popleft()
        if u in final:
            return d[u]
        for v in adjMat[u]:
            if d[v] > d[u] + 1:
                d[v] = d[u] + 1
                frontier.append(v)
    raise Exception("not supposed to happen") # not supposed to happen as L is non empty

print(findShortestLength())
