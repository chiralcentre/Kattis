from sys import stdin,stdout
from collections import deque

H = 100000

def compress(x,y):
    return x * H + y

def decompress(v):
    return v // H, v % H

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.numSets = 1
        
    def findSet(self,j):
        if self.p[j] == j:
            return j
        else:
            self.p[j] = self.findSet(self.p[j])
            return self.p[j]

    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self,i,j):
        if not self.isSameSet(i,j):
            x,y = self.findSet(i),self.findSet(j)
            # rank is used to keep tree short
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
            self.numSets -= 1
            
N = int(stdin.readline())
points = set()
for i in range(N):
    x,y = map(int,stdin.readline().split())
    points.add(compress(x,y))
grid = [[-1 for i in range(1000)] for j in range(1000)]
mappings = [0 for i in range(100001)]
frontier = deque([])
counter = 0
for p in points:
    x,y = decompress(p)
    grid[x][y] = counter
    frontier.append(p)
    mappings[counter] = p # mappings[a] represents the compressed value of the ath point
    counter += 1
while frontier:
    x,y = decompress(frontier.popleft())
    for u,v in possiblepositions(x,y,1000,1000,grid):
        if grid[u][v] == -1:
            grid[u][v] = grid[x][y]
            frontier.append(compress(u,v))
edges = []
for i in range(999):
    for j in range(1000):
        if grid[i][j] != grid[i + 1][j]:
            a,b = decompress(mappings[grid[i][j]])
            c,d = decompress(mappings[grid[i + 1][j]])
            edges.append((compress(grid[i][j],grid[i + 1][j]),abs(a - c) + abs(b - d)))
        if grid[j][i] != grid[j][i + 1]:
            a,b = decompress(mappings[grid[j][i]])
            c,d = decompress(mappings[grid[j][i + 1]])
            edges.append((compress(grid[j][i],grid[j][i + 1]),abs(a - c) + abs(b - d)))
edges.sort(key = lambda x: x[1]) # sort in ascending order of edge weight
UFDS = UnionFind(len(points))
ans = 0
for r,w in edges:
    u,v = decompress(r)
    if not UFDS.isSameSet(u,v):
        ans += w
        UFDS.unionSet(u,v)
    if UFDS.numSets == 1:
        break
stdout.write(f"{ans}\n")

