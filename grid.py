from sys import stdin
from collections import deque

def possiblepositions(i,j,r,c,board):
    k = int(board[i][j])
    movements = [(-k,0),(k,0),(0,-k),(0,k)]
    return [(i + x,j + y) for x,y in movements if i + x in range(r) and j + y in range(c)]

def minmoves(board):
    r,c = len(board),len(board[0])
    visited = [[False for _ in range(m)] for j in range(n)] #record positions visited before, starting from top left corner
    visited[0][0] = True
    #use a queue for BFS
    frontier = deque([(0,0,0)]) # all possible neighbours we want to try
    # right coordinate keeps track of number of jumps
    while frontier:
        a,b,counter = frontier.popleft() 
        if a == r-1 and b == c-1:
            return counter
        for x,y in possiblepositions(a,b,r,c,board):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y,counter+1))
    return -1


n,m = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for i in range(n)]
print(minmoves(grid))
