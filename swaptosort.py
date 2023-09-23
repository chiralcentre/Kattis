from sys import stdin,stdout

class UnionFind:
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
                            
N,K = map(int,stdin.readline().split())
UFDS = UnionFind(N) 
for _ in range(K): #pairs can be done in any order
    a,b = map(int,stdin.readline().split())
    UFDS.unionSet(a-1,b-1)
# array can only be sorted in increasing order if i and n-i-1 are in the same set for all i
possible = True
for i in range(N >> 1):
    if UFDS.findSet(i) != UFDS.findSet(N-i-1):
        possible = False
        break
stdout.write("Yes\n") if possible else stdout.write("No\n")
