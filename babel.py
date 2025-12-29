from sys import stdin,stdout

# algorithm runs in O(RC + Q) time
movements = [(-1,0),(0,1),(1,0),(0,-1)]
    
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

R,C = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(R)]
components = [[-1 for j in range(C)] for i in range(R)]
CC = 0
for i in range(R):
    for j in range(C):
        if components[i][j] == -1:
            frontier = [(i,j)]
            components[i][j] = CC
            while frontier:
                a,b = frontier.pop()
                for x,y in possiblepositions(a,b,R,C,grid):
                    if components[x][y] == -1 and grid[x][y] == grid[i][j]:
                        frontier.append((x,y))
                        components[x][y] = CC
            CC += 1
for _ in range(int(stdin.readline())):
    r1,c1,r2,c2 = map(int,stdin.readline().split())
    stdout.write(f"{grid[r1][c1]}\n") if components[r1][c1] == components[r2][c2] else stdout.write("N\n")
