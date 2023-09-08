from sys import stdin,stdout

UPPER = 1000000
class UnionFind:
    def __init__(self,N):
        self.p = [i for i in range(N)]
        self.rank = [0 for i in range(N)]
        self.num_disjoint = N
        
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
            self.num_disjoint -= 1
            return True
        return False
    
# rephrase the question: given N vertices, and M edges, is it possible to rearrange K <= M edges such that all N vertices are connected?
# this is only possible if M >= N - 1, since the minimum number of edges in a connected component with N vertices is N - 1
N,M = map(int,stdin.readline().split())
if M < N - 1:
    stdout.write("Nej\n")
else:
    UFDS,cycle_edges = UnionFind(N),[]
    for i in range(M):
        u,v = map(int,stdin.readline().split())
        u -= 1; v -= 1
        if not UFDS.unionSet(u,v):
            cycle_edges.append(u * UPPER + v)
    # labels[i] stores the number of a vertex in the ith component
    labels = {UFDS.findSet(i) for i in range(N)}
    labels = list(labels) 
    # number of edges that need to be arranged = number of connected components - 1
    # check if there are sufficient cycle edges to break
    if len(cycle_edges) < UFDS.num_disjoint - 1:
        stdout.write("Nej\n")
    else:
        stdout.write("Ja\n")
        stdout.write(f"{UFDS.num_disjoint - 1}\n")
        for i in range(UFDS.num_disjoint - 1):
            # connect the ith CC with (i + 1)th CC
            u,v = labels[i],labels[i + 1]
            pu,pv = cycle_edges[i] // UPPER, cycle_edges[i] % UPPER
            # take edges from cycles
            stdout.write(f"{pu + 1} {pv + 1} {u + 1} {v + 1}\n")
