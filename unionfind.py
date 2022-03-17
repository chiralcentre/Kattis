from sys import stdin,stdout

class UnionFind:
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
                            
N,Q = map(int,stdin.readline().split())
UFDS = UnionFind(N)
for _ in range(Q):
    op,a,b = stdin.readline().split()
    if op == '=':
        UFDS.unionSet(int(a),int(b))
    else: #'?' command
        stdout.write('yes\n') if UFDS.isSameSet(int(a),int(b)) else stdout.write('no\n')
        
