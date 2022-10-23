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
                
for line in stdin:
    n,r,a,b,c = map(int,line.split())
    UFDS = UnionFind(n)
    for i in range(n):
        x,y = 0,0
        while x == y:
            r = (r * a + b) % c
            x = r % n
            r = (r * a + b) % c
            y = r % n
        UFDS.unionSet(x,y)
    group_sizes,connected = {},0
    for i in range(n):
        if UFDS.numElems[i] > 0:
            group_sizes[UFDS.numElems[i]] = 1 if UFDS.numElems[i] not in group_sizes else group_sizes[UFDS.numElems[i]] + 1
            connected += 1
    result = [str(connected)]
    for key,value in sorted(group_sizes.items(),key = lambda x: (-x[0])): #sort in reverse order
        result.append(str(key)) if value == 1 else result.append(f"{key}x{value}")
    stdout.write(" ".join(s for s in result) + "\n")
    
