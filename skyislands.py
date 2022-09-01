from sys import stdin,stdout

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
                    
N,M = map(int,stdin.readline().split())
UFDS = UnionFind(N); connected = 1
for i in range(M):
    a,b = map(lambda x: int(x) - 1, stdin.readline().split())
    if not UFDS.isSameSet(a,b):
        connected += 1
        UFDS.unionSet(a,b)
stdout.write("YES") if connected == N else stdout.write("NO")

