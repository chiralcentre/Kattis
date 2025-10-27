from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1),
             (-1,-1),(-1,1),(1,-1),(1,1)]

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

N,M = int(stdin.readline()),int(stdin.readline())
buildings = [stdin.readline().strip() for _ in range(N)]
unpowered = []
for i in range(N):
    for j in range(M):
        if buildings[i][j] != "T":
            for x,y in possiblepositions(i,j,N,M,buildings):
                if buildings[x][y] == "T":
                    break
            else:
                unpowered.append((i,j))
if unpowered:
    stdout.write("False\n")
    for x,y in unpowered:
        stdout.write(f"{x} {y}\n")
else:
    stdout.write("True\n")
