from sys import stdin,stdout
#runtime of 2.74s
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
                    
#Kruskal's algorithm is used to construct MST and find maximum weight along minimax path
n,m = map(int,stdin.readline().split())
UFDS = UnionFind(n)
# sort by edge weights, O(m log m)
edgeList = sorted([(lambda x: (int(x[0]),int(x[1]),int(x[2])))(stdin.readline().split()) for i in range(m)],key = lambda y: y[2])
E,maxRange = 0,0 
for u,v,w in edgeList:#O(m alpha(n)) where alpha(n) is the inverse Ackermann function
    if not UFDS.isSameSet(u,v):
        E += 1
        if w > maxRange:
            maxRange = w
        UFDS.unionSet(u,v)
# a MST will have n - 1 edges
stdout.write("IMPOSSIBLE\n") if E != n - 1 else stdout.write(f"{maxRange}\n")

