from sys import stdin,stdout

class UnionFind: #UFDS is used
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.disjointSets = N
        
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
            self.disjointSets -= 1

for _ in range(int(stdin.readline())):
    m = int(stdin.readline())
    roads = UnionFind(m)
    for i in range(int(stdin.readline())):
        a,b = map(int,stdin.readline().split())
        roads.unionSet(a,b)
    stdout.write(f'{roads.disjointSets-1}\n') #number of edges to add = number of disjointSets - 1
