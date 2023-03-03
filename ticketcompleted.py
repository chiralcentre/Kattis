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
                    
#count components and the size of each component in O(N + M) time, assuming UFDS operations are almost constant
N,M = map(int,stdin.readline().split())
UFDS,adjList = UnionFind(N),[[] for _ in range(N)]
for i in range(M):
    a,b = map(lambda x: int(x) - 1, stdin.readline().split())
    adjList[a].append(b)
    adjList[b].append(a)
#perform iterative DFS
frontier,visited = [],[False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        frontier.append(i)
        while frontier:
            u = frontier.pop()
            for v in adjList[u]:
                if not visited[v]:
                    visited[v] = True
                    frontier.append(v)
                    UFDS.unionSet(u,v)
#divide by total possibilities
total = N*(N - 1)//2
earnPointsTickets = sum(v * (v - 1)//2 for v in UFDS.numElems)
stdout.write(f"{earnPointsTickets/total}\n")
