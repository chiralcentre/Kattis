from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

R,C = map(int,stdin.readline().split())
town = [stdin.readline().strip() for _ in range(R)]
contaminated = set()
for i in range(R):
    for j in range(C):
        if town[i][j] == "O":
            for x,y in possiblepositions(i,j,R,C,town):
                if town[x][y] == "W":
                    contaminated.add((x * C + y))
print(len(contaminated))
