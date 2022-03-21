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

for i in range(int(stdin.readline())):
    F = int(stdin.readline())
    network = UnionFind(2*F) #maximum 2F unique friends
    persons,counter = {},0 #dictionary is used to map person names to integer index
    for j in range(F):
        p1,p2 = stdin.readline().split()
        for p in (p1,p2):
            if p not in persons:
                persons[p] = counter
                counter += 1
        network.unionSet(persons[p1],persons[p2])
        stdout.write(f'{network.numberOfElems(persons[p1])}\n') #p1 and p2 are in the same set

    
