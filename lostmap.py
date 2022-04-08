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
                    
n,edgeList,E = int(stdin.readline()),[],0
for i in range(n):
    weights = stdin.readline().split()
    for j in range(i+1,n): #only need to consider one half due to symmetry
        edgeList.append((i,j,int(weights[j])))
edgeList.sort(key = lambda x: x[2]) # sort by edge weight
UFDS = UnionFind(n)
# run Kruskal's
for u,v,w in edgeList:
    if E == n - 1: #MST found
        break 
    if not UFDS.isSameSet(u,v):
        UFDS.unionSet(u,v); E += 1;
        stdout.write(f'{u+1} {v+1}\n') #no need to store MST, print out as the algorithm is running

