from sys import stdin

class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.setSize = [1 for i in range(N)]
        self.isActive = [False for _ in range(N)]
        self.numActiveComponents = 0
        self.activeCount = 0

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
            return True
        return False

    def activate(self,r,c,N):
        h1 = compress(r,c,N)
        self.isActive[h1] = True
        self.activeCount += 1
        self.numActiveComponents += 1
        for x,y in possiblepositions(r,c,N,N):
            h2 = compress(x,y,N)
            if self.isActive[h2]:
                res = self.unionSet(h1,h2)
                if res: # combined into same set
                    self.numActiveComponents -= 1
                    
    def sizeOfSet(self,i):
        return self.setSize[self.findSet(i)]
    
movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def compress(i,j,N):
    return i * N + j

def decompress(H,N):
    return H // N, H % N

# sort values in descending order
# build up active set incrementally by starting from highest valued cells
# size of active set is only guaranteed to increase and not decrease
# code runs in O(N^2 * inverseAckermann(N^2))
def solve(N,coords):
    desc_values = sorted(coords.keys(),reverse = True)
    UFDS = UnionFind(N * N)
    for v in desc_values:
        for a,b in coords[v]:
            UFDS.activate(a,b,N)
        if UFDS.activeCount >= N and UFDS.numActiveComponents == 1:
            return v
    raise Exception("not supposed to happen")

N = int(stdin.readline())
coords = {}
for i in range(N):
    row = list(map(int,stdin.readline().split()))
    for j in range(N):
        if row[j] not in coords:
            coords[row[j]] = [(i,j)]
        else:
            coords[row[j]].append((i,j))
print(solve(N,coords))
