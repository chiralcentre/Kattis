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

N = int(stdin.readline())
UFDS = UnionFind(500001) #ingredients can be from 0 to 500000 inclusively
concoct = 0
#O(NM)
for i in range(N):
    M,*ingredients = map(int,stdin.readline().split())
    parents = {UFDS.findSet(ingredients[j]-1) for j in range(M)} #O(M)
    #O(M)
    #in order for a potion to be made, the sum of size of contents for ingredients must add up to M
    if sum(UFDS.numElems[k] for k in parents) ==  M: 
        concoct += 1
        for j in range(M-1):
            UFDS.unionSet(ingredients[j]-1,ingredients[j+1]-1)
stdout.write(str(concoct))
    
