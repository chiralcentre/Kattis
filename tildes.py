from sys import stdin,stdout

class UnionFind: #UFDS is used
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.numElems = [1 for i in range(N)]

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
                self.numElems[x] += self.numElems[y]
                self.numElems[y] = 0
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                self.numElems[y] += self.numElems[x]
                self.numElems[x] = 0

n,q = map(int,stdin.readline().split())
UFDS = UnionFind(n)
for i in range(q):
    line = stdin.readline().split()
    if line[0] == "t":
        a,b = int(line[1]) - 1,int(line[2]) - 1
        UFDS.unionSet(a,b)
    else:
        stdout.write(f"{UFDS.numElems[UFDS.findSet(int(line[1])-1)]}\n")
