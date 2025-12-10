from sys import stdin,stdout
from math import sqrt

movements = [(-1,0),(0,1),(1,0),(0,-1)]
def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def solve(names):
    L = round(sqrt(len(names)))
    grid = [["" for i in range(L)] for j in range(L)]
    for i in range(len(names)):
        r,c = i // L, i % L
        grid[r][c] = names[i]
    for i in range(L):
        for j in range(L):
            found = True
            for x,y in possiblepositions(i,j,L,L):
                if len(grid[x][y]) != len(grid[i][j]):
                    found = False
                    break
            if found:
                return grid[i][j]
    return "Name Not Found"

for _ in range(int(stdin.readline())):
    stdout.write(f"{solve(stdin.readline().split())}\n")
                
            
