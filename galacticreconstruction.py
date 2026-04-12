from sys import stdin,stdout

class UnionFind:
    def __init__(self,N,wealths):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.numSets = N
        self.setWealth = wealths[:]

    def findSet(self,j):
        if self.p[j] == j:
            return j
        else:
            self.p[j] = self.findSet(self.p[j])
            return self.p[j]

    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self,i,j,c):
        if not self.isSameSet(i,j):
            x,y = self.findSet(i),self.findSet(j)
            if self.setWealth[x] < c or self.setWealth[y] < c:
                return "IMPOSSIBLE"
            # invariant: rank(x) <= rank(y)
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            self.p[x] = y
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1
            self.setSize[y] += self.setSize[x]
            self.setWealth[y] += self.setWealth[x] - 2 * c
            self.numSets -= 1
            return "BUILT"
        else:
            return "UNNECESSARY"

    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]

    def wealthOfSet(self, i):
        return self.setWealth[self.findSet(i)]

n,m = map(int,stdin.readline().split())
wealths = list(map(int,stdin.readline().split()))
UFDS = UnionFind(n,wealths)
for _ in range(m):
    u,v,c = map(int,stdin.readline().split())
    u -= 1; v -= 1
    stdout.write(f"{UFDS.unionSet(u,v,c)}\n")
