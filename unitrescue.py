from sys import stdin
from fractions import Fraction

def solve(counter,s,e,adjList,mappings):
    if s not in mappings or e not in mappings:
        return "IMPOSSIBLE"
    s,e = mappings[s],mappings[e]
    frontier,visited = [s],[-1 for _ in range(counter)]
    visited[s] = a
    while frontier:
        u = frontier.pop()
        for v,r in adjList[u]:
            if visited[v] == -1:
                visited[v] = r * visited[u]
                frontier.append(v)
            if v == e:
                return str(float(visited[v]))
    return "IMPOSSIBLE"
    
mappings = {}
counter,adjList = 0,[]
for i in range(int(stdin.readline())):
    a,b,m,d = stdin.readline().split()
    m,d = int(m),int(d)
    if a not in mappings:
        mappings[a] = counter
        counter += 1
        adjList.append([])
    if b not in mappings:
        mappings[b] = counter
        counter += 1
        adjList.append([])
    u,v = mappings[a],mappings[b]
    adjList[u].append((v,Fraction(m,d)))
    adjList[v].append((u,Fraction(d,m)))
a,s,e = stdin.readline().split()
a = Fraction(a)
print(solve(counter,s,e,adjList,mappings))
