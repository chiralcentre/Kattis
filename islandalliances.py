from sys import stdin,stdout

'''
From Solution Outlines:
We would like to keep track of which pairs of states contain islands whose inhabitants distrust each
other, and for this purpose we keep an (unordered) edge set for each state A’s root island containing
edges to all the root islands of states B such that some pair of islands in A and B distrust each
other. For example, if A is a state that currently contains islands a1 and a2, where a1 is at the root
of the state’s tree in the disjoint set forest, and B is a state currently only containing the island b1,
then if the inhabitants of the islands a2 and b1 distrust each other then a1 should have an edge to
b1, and vice versa.
In the beginning, each state only contains a single island and so each island is at the root of its
state’s tree. This means that the edge sets should simply contain all the M pairs of islands given in
the input.
However, when two states with root islands a and b are merged, where a is chosen as the root
of the new merged state, then all edges (b, c) should be replaced by edges (a, c). This is done by
simply iterating over all of b’s incident edges, removing them from the sets of both endpoints, and
finally adding the updated edges
Use union-by-rank or union-by-size. To see why this is efficient enough, note that as
long as our union find implementation uses either union-by-rank or union-by-size when merging two
sets, the number of times any particular island will get a new root island representing its state is
bounded by log N. This implies that the number of times any particular edge needs to be updated,
because either of its endpoints gets a new root island, is bounded by 2 log N. Hence, the time
complexity of updating the edges is O(M log N).
'''

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
                return (x,y)
            else:
                self.p[x] = y
                if self.rank[x] == self.rank[y]:
                    self.rank[y] += 1
                return (y,x)

#Overall time complexity is O(M log N + (N + Q) alpha(N))
n,m,q = map(int,stdin.readline().split())
UFDS = UnionFind(n)
adjList = [set() for _ in range(n)]
for i in range(m):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[u].add(v)
    adjList[v].add(u)
    
for i in range(q):
    u,v = map(lambda x: int(x) - 1, stdin.readline().split())
    u,v = UFDS.findSet(u),UFDS.findSet(v)
    if u in adjList[v]:
        stdout.write("REFUSE\n")
    else:
        stdout.write("APPROVE\n")
        a,b = UFDS.unionSet(u,v) #a is chosen as new root
        #remove all edges (b,c) and replace with (a,c)
        for c in adjList[b]:
            adjList[c].remove(b)
            adjList[c].add(a)
            adjList[a].add(c)
        adjList[b] = set() 
