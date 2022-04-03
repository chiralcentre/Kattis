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
          
while True:
    n,m = map(int,stdin.readline().split())
    if n == m == 0:
        break
    UFDS = UnionFind(n)
    # sort by edge weights for Kruskal's algorithm, O(m log m)
    edgeList = sorted([(lambda x: (int(x[0]),int(x[1]),int(x[2])))(stdin.readline().split()) for i in range(m)],key = lambda y: y[2]) 
    MST,E,cost = [],0,0
    for u,v,w in edgeList:#O(m)
        if not UFDS.isSameSet(u,v):
            cost += w; E += 1;
            MST.append((min(u,v),max(u,v))) # arrange such that left element < right element
            UFDS.unionSet(u,v)
    MST.sort() #sort by lexicographical order, O(n log n)
    if E != n - 1: # a MST will have n - 1 edges
        stdout.write("Impossible\n")
    else:
        stdout.write(f"{cost}\n")
        for start,end in MST:
            stdout.write(f"{start} {end}\n")
            
    
