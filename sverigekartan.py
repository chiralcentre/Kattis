from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
    
class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]

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
                self.setSize[x] += self.setSize[y]
                self.setSize[y] = 0
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                self.setSize[y] += self.setSize[x]
                self.setSize[x] = 0
            return True
        else:
            return False # no union was done
        
    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]
    
def findStart(grid,R,C):
    for i in range(R):
        for j in range(C):
            if grid[i][j] == "S":
                return (i,j)
    return (-1,-1)

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i+x][j+y] != "."]

# code runs in O(RC + U), assuming UFDS operations are in constant time
R,C,U = [int(stdin.readline()) for _ in range(3)]
grid = [list(stdin.readline().strip()) for _ in range(R)]
UFDS = UnionFind(R * C)
sx,sy = findStart(grid,R,C)
frontier,S = [(sx,sy)],sx * C + sy
while frontier:
    x,y = frontier.pop()
    for a,b in possiblepositions(x,y,R,C,grid):
        res = UFDS.unionSet(x * C + y, a * C + b)
        if res:
            frontier.append((a,b))
stdout.write(f"{UFDS.sizeOfSet(S)}\n")
# handle the U queries
for i in range(U):
    # offset by 1 due to zero indexing
    x,y = map(lambda x: int(x) - 1,stdin.readline().split())
    grid[x][y] = "#"
    frontier = [(x,y)]
    while frontier:
        c,d = frontier.pop()
        for a,b in possiblepositions(c,d,R,C,grid):
            res = UFDS.unionSet(c * C + d, a * C + b)
            if res:
                frontier.append((a,b))
    stdout.write(f"{UFDS.sizeOfSet(S)}\n")
    
    
