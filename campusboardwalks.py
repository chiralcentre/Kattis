from sys import stdin

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

# find MST in O(b log b) time
n,s,b = map(int,stdin.readline().split())
edgeList,UFDS = [],UnionFind(n)
for _ in range(s):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    # union the sets together
    UFDS.unionSet(u,v)
for i in range(b):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1
    edgeList.append((u,v,w))
edgeList.sort(key = lambda x: x[2])
cost = 0
for u,v,w in edgeList:
    if UFDS.numSets == 1:
        break
    if not UFDS.isSameSet(u,v):
        cost += w
        UFDS.unionSet(u,v)
print("more boardwalks needed!" if UFDS.numSets != 1 else str(cost)) 
