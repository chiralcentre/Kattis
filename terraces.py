from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.numSets = N

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
            # invariant: rank(x) <= rank(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.setSize[y] += self.setSize[x]
            self.numSets -= 1

    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]

c,r = map(int,stdin.readline().split())
grid = [list(map(int,stdin.readline().split())) for _ in range(r)]
# the coordinates are linearised in the following fashion for UFDS: (row number) * c + column number
visited,UFDS = [[False for i in range(c)] for j in range(r)],UnionFind(r*c)
ans = 0
for i in range(r): #total time complexity is O(rc)
    for j in range(c):
        if not visited[i][j]: #perform iterative DFS
            canFlow = False
            visited[i][j] = True
            frontier = [(i,j)]
            while frontier:
                a,b = frontier.pop()
                for x,y in possiblepositions(a,b,r,c,grid):
                    if grid[x][y] == grid[i][j] and not visited[x][y]:
                        visited[x][y] = True
                        frontier.append((x,y))
                        UFDS.unionSet(i * c + j,x * c + y)
                    elif grid[x][y] < grid[i][j]: # can flow downwards
                        canFlow = True
            if not canFlow:
                ans += UFDS.sizeOfSet(i * c + j)
stdout.write(f"{ans}\n")
                        
