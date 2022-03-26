from sys import stdin,stdout
#UFDS skeleton code was copied over from almostunionfind, and hence some methods are not relevant to this question.
class UnionFind:
    def __init__(self,N):
        self.p2 = [i for i in range(N)] #keeps track of original parent when a move is made
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.numElems = [1 for i in range(N)]
        self.total = [i for i in range(N)]

    def findSet(self,j):
        a = self.p2[j]
        b = self.p[a]
        while a != b:
            self.p[a] = self.p[b]
            a = self.p[a]
            b = self.p[a]
        return a
        
    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)

    def unionSet(self,i,j):
        if not self.isSameSet(i,j):
            x,y = self.findSet(i),self.findSet(j)
            # union by rank
            if self.rank[x] > self.rank[y]:
                x,y = y,x
            self.p[y] = x
            self.numElems[x] += self.numElems[y]
            self.numElems[y] = 0
            self.total[x] += self.total[y]
            self.total[y] = 0
        
    def move(self,a,b): 
        if not self.isSameSet(a,b):
            x,y = self.findSet(a),self.findSet(b)
            self.numElems[y] += 1
            self.numElems[x] -= 1
            self.total[y] += a
            self.total[x] -= a
            self.p2[a] = y
        
    def numberOfElems(self,i):
        return self.numElems[self.findSet(i)]

    def elemSum(self,i): # add back due to zero indexing
        return self.total[self.findSet(i)] + self.numberOfElems(i)


F = int(stdin.readline())
buildings = UnionFind(2*F) #maximum 2F unique buildings
names,counter = {},0 #dictionary is used to map building names to integer index
for j in range(F):
    b1,b2 = stdin.readline().split()
    for b in (b1,b2):
        if b not in names:
            names[b] = counter
            counter += 1
    buildings.unionSet(names[b1],names[b2])
    stdout.write(f'{buildings.numberOfElems(names[b1])}\n') #b1 and b2 are in the same set
