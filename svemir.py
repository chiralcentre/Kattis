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
          

#tunnels only need to be constructed between planets who are immediate neighbors on one of the axis.
N = int(stdin.readline())
planets = []
for i in range(N):
    x,y,z = map(int,stdin.readline().split())
    planets.append((x,y,z,i)) #i is the index of the point
planetX = sorted(planets,key = lambda x: x[0]) #sort by x coordinate in O(N log N)
planetY = sorted(planets,key = lambda x: x[1]) #sort by y coordinate in O(N log N)
planetZ = sorted(planets,key = lambda x: x[2]) #sort by z coordinate in O(N log N)
#use Kruskal's algorithm in O((3N-3)log(3N-3)) = O(N log N) since there is a total of 3N - 3 edges
edgeList = []
for i in range(N-1):
    edgeList.append((planetX[i][3],planetX[i+1][3],planetX[i+1][0] - planetX[i][0]))
    edgeList.append((planetY[i][3],planetY[i+1][3],planetY[i+1][1] - planetY[i][1]))
    edgeList.append((planetZ[i][3],planetZ[i+1][3],planetZ[i+1][2] - planetZ[i][2]))

edgeList.sort(key = lambda x: x[2]) #sort by edge weights in O(N log N)
UFDS = UnionFind(N)
cost,E = 0,0
for u,v,w in edgeList: #O(N)
    if not UFDS.isSameSet(u,v):
        cost += w; E += 1;
        UFDS.unionSet(u,v)
        if E == N - 1: #complete MST is formed
            break
stdout.write(f'{cost}')
