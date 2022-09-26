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

def solve(n,m,insecure,secureEL,insecureEL):
    #let number of secure edges and number of insecure edge be S,L, S + L = m
    #sort in ascending order of weight in O(S log S) time
    secureEL.sort(key = lambda x: x[2])
    #sort in ascending order of weight in O(L log L) time
    insecureEL.sort(key = lambda x: x[2])
    if m == 1: #only one edge
        return "impossible" if n > 2 else str(insecureEL[0][2]) if insecureEL else str(secureEL[0][2])
    UFDS = UnionFind(n)
    E,cost = 0,0
    for u,v,w in secureEL:#O(S alpha(n)) where alpha(n) is the inverse Ackermann function
        if E == n - 1 - len(insecure): #optimisation
            break
        if not UFDS.isSameSet(u,v):
            E += 1; cost += w
            UFDS.unionSet(u,v)
    if E != max(0,n - 1 - len(insecure)): #not all secure buildings are connected
        return "impossible"
    for u,v,w in insecureEL:#O(L alpha(n)) where alpha(n) is the inverse Ackermann function
        if E == n - 1: #optimisation
            break
        if not UFDS.isSameSet(u,v) and ((u in insecure and v not in insecure) or (u not in insecure and v in insecure)): #only one edge vertex cna be insecure
            E += 1; cost += w
            UFDS.unionSet(u,v)
    if E != n - 1: #not all insecure buildings can be connected
        return "impossible"
    return str(cost)
                    
#Kruskal's algorithm is used              
n,m,p = map(int,stdin.readline().split())
#offset by 1 due to zero indexing
insecure = set(map(lambda x: int(x) - 1,stdin.readline().split()))
secureEL,insecureEL = [],[]
for i in range(m):
    u,v,w = map(int,stdin.readline().split())
    u -= 1; v -= 1 #offset by 1 due to zero indexing
    if u != v: #prevent self loops
        insecureEL.append((u,v,w)) if u in insecure or v in insecure else secureEL.append((u,v,w))
stdout.write(solve(n,m,insecure,secureEL,insecureEL))
