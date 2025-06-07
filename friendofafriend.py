from sys import stdin,stdout

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

n,m = map(int,stdin.readline().split())
UFDS = UnionFind(n)
adjList = [set() for _ in range(n)]
for i in range(m):
    c,x,y = stdin.readline().split()
    x,y = map(int,[x,y])
    if c == "f":
        adjList[x].add(y)
        adjList[y].add(x)
        UFDS.unionSet(x,y)
    else:
        sign = "?" if not UFDS.isSameSet(x,y) else "+" if x in adjList[y] else "-"
        stdout.write(f"{x} {sign} {y}\n")
