from sys import stdin,stdout
from collections import deque

def chessRow(r):
    return 8 - r

def chessCol(c):
    return chr(c + 97)

def possiblepositions(i,j,r,c):
    movements = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def BFS(start_x,start_y,r,c):
    visited = [[-1 for i in range(c)] for j in range(r)]
    frontier = deque([(start_x,start_y,0)]) #third coordinate keeps track of number of jumps
    visited[start_x][start_y] = 0
    ans = []
    while frontier: 
        i,j,counter = frontier.popleft()
        found = False
        for a,b in possiblepositions(i,j,r,c):
            if visited[a][b] == -1:
                frontier.append((a,b,counter+1))
                visited[a][b] = counter + 1
                found = True
    highest = max(max(row) for row in visited)
    ans = [(i,j) for i in range(8) for j in range(8) if visited[i][j] == highest]
    return ans,highest

for _ in range(int(stdin.readline())):
    c,r = list(stdin.readline().strip())
    r,c = 8 - int(r), ord(c) - 97
    ans,moves = BFS(r,c,8,8)
    final = [str(moves)]
    for i,j in ans:
        final.append(chessCol(j) + str(chessRow(i)))
    stdout.write(" ".join(elem for elem in final))
    stdout.write("\n")
