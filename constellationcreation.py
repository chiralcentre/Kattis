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
            return True
        else:
            return False

r,c,n = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
output = [[" " for i in range(c)] for j in range(r)]
UFDS = UnionFind(r * c)
# group stars by rows and columns
t,rows,cols = 0,[[] for i in range(r)],[[] for j in range(c)]
for i in range(r):
    for j in range(c):
        if grid[i][j] == "*":
            t += 1
            output[i][j] = "*"
            rows[i].append(j)
            cols[j].append(i)

# use UFDS to check if stars are in same constellation
# decrease by 1 whenever stars from different constellations are joined together
for i in range(r):
    if t == n:
        break
    if rows[i]:
        y = rows[i][0]
        for j in range(1,len(rows[i])):
            cy = rows[i][j]
            if UFDS.unionSet(i * c + y, i * c + cy):
                for k in range(y + 1, cy):
                    output[i][k] = "-"
                t -= 1
                if t == n:
                    break
            y = cy
    
for j in range(c):
    if t == n:
        break
    if cols[j]:
        x = cols[j][0]
        for i in range(1,len(cols[j])):
            cx = cols[j][i]
            if UFDS.unionSet(x * c + j, cx * c + j):
                for k in range(x + 1, cx):
                    output[k][j] = "|" if output[k][j] == " " else "+"
                t -= 1
                if t == n:
                    break
            x = cx
            
stdout.write("\n".join("".join(row) for row in output))
            
    
