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

# use Kruskal's algorihm in O(E log E) time
n,m = map(int,stdin.readline().split())
UFDS = UnionFind(n)
edge_list = []
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1
    edge_list.append((u,v,w,i + 1))
edge_list.sort(key = lambda x: x[2])
chosen = []
for u,v,w,i in edge_list:
    if not UFDS.isSameSet(u,v):
        chosen.append(i)
        UFDS.unionSet(u,v)
    # early optimisation
    if len(chosen) == n - 1:
        break
stdout.write(f"{len(chosen)}\n")
for label in chosen:
    stdout.write(f"{label}\n")
