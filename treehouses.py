from sys import stdin,stdout
from math import sqrt

class UnionFind: #UFDS is used
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
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
            # rank is used to keep tree short
            if self.rank[x] > self.rank[y]:
                self.p[y] = x
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
            self.numSets -= 1
                    
#Kruskal's algorithm is used to construct MST in O(n^2 log n)
n,e,p = map(int,stdin.readline().split())
e -= 1 # subtract 1 due to zero indexing
points = [tuple(map(float,stdin.readline().split())) for _ in range(n)]
UFDS = UnionFind(n)
# connect houses from 0 to e together
# houses from 0 to e inclusive do not need cables between them
for i in range(1,e + 1):
    UFDS.unionSet(0,i)
for i in range(p):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    UFDS.unionSet(u,v)
    
edgeList = []
for i in range(n):
    for j in range(max(e + 1,i + 1),n):
        if not UFDS.isSameSet(i,j): # check if the houses are already connected
            x,y = points[i]
            nx,ny = points[j]
            edgeList.append((i * 1000 + j,sqrt((x - nx) ** 2 + (y - ny) ** 2)))
            
edgeList.sort(key = lambda x: x[1]) #sort in increasing order of weight
ans = 0
for res,w in edgeList:
    u,v = res // 1000, res % 1000
    if UFDS.numSets == 1:
        break
    if not UFDS.isSameSet(u,v):
        UFDS.unionSet(u,v)
        ans += w
stdout.write(f"{ans}\n")
