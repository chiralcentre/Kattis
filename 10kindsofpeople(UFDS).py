from sys import stdin,stdout

def possiblepositions(i,j,r,c,grid):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] == grid[i][j]] #last condition checks for same component
#iterative DFS
def DFS(i,j,r,c,visited,grid,UFDS):
    visited[i][j] = True
    frontier = [(i,j)]
    while frontier:
        a,b = frontier.pop()
        for x,y in possiblepositions(a,b,r,c,grid):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y))
                UFDS.unionSet(i*c+j,x*c+y)

class UnionFind: #UFDS is used
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]

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

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
# the coordinates are linearised in the following fashion for UFDS: (row number) * c + column number
visited,UFDS = [[False for i in range(c)] for j in range(r)],UnionFind(r*c)
for i in range(r): #total time complexity is O(5RC) = O(RC)
    for j in range(c):
        if not visited[i][j]: #perform DFS 
            DFS(i,j,r,c,visited,grid,UFDS)

for i in range(int(stdin.readline())): #each query can be answered in O(1) time
    x1,y1,x2,y2 = map(lambda x: int(x) - 1, stdin.readline().split()) #offset by 1 due to zero indexing
    if UFDS.isSameSet(x1*c+y1,x2*c+y2):
        stdout.write("binary\n") if grid[x1][y1] == '0' else stdout.write("decimal\n")
    else:
        stdout.write("neither\n")
