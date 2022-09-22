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
                
alphabet_mapping = {chr(i): i - 65 for i in range(65,91)}
N,M,K = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(N)]
UFDS = UnionFind(K)
#go column by column, and union every class in the same column into the same set
#O(MN)
for i in range(M):
    first_class = alphabet_mapping[grid[0][i]]
    for j in range(1,N):
        UFDS.unionSet(first_class,alphabet_mapping[grid[j][i]])
#O(K)
counter = 0
for i in range(K):
    if UFDS.numElems[i] > 0:
        counter += 1
stdout.write(str(counter))
        

