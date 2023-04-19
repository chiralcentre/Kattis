from sys import stdin,stdout

class UnionFind: #UFDS is used
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

#go through all queries and identify all edges to be removed and remove from graph
#label the components after all edges are removed in O(Q + M*alpha(N))
#start from last query and move backwards to first query, adding edges for each query to delete an edge
#all queries can be answered in O(Q*alpha(N))
N,M,Q = map(int,stdin.readline().split())
UFDS = UnionFind(N)
edgeList = set()
#use coordinate compression since hashing of tuples is computationally expensive
for _ in range(M):
    u,v = map(int,stdin.readline().split())
    edgeList.add(u * N + v)
queries = []
#coordinate compression again
for i in range(Q):
    t,u,v = map(int,stdin.readline().split())
    if t == 0:
        edgeList.discard(u * N + v)
        edgeList.discard(v * N + u)
    queries.append((t,u * N + v))
#decompress
for r in edgeList:
    UFDS.unionSet(r // N, r % N)
ans = []
#decompress
for i in range(Q - 1, -1, -1):
    t,r = queries[i]
    u,v = r // N, r % N
    if t == 0:
        UFDS.unionSet(u,v)
    else:
        ans.append("safe\n") if UFDS.isSameSet(u,v) else ans.append("unsafe\n")
for i in range(len(ans) - 1, -1, -1):
    stdout.write(ans[i])
