from sys import stdin
from collections import deque

def possiblepositions(pos,board):
    k = int(board[pos[0]][pos[1]])
    movements = [(-k,0),(k,0),(0,-k),(0,k)]
    return [(pos[0] + x,pos[1] + y) for x,y in movements if pos[0] + x in range(len(board)) and pos[1] + y in range(len(board[0]))]

def minmoves(board):
    r,c = len(board),len(board[0])
    visited = [[False for _ in range(m)] for j in range(n)] #record positions visited before, starting from top left corner
    visited[0][0] = True
    frontier = deque([(0,0,0)]) # all possible neighbours we want to try
    # right coordinate keeps track of number of jumps
    while frontier:
        a,b,counter = frontier.popleft() 
        if a == r-1 and b == c-1:
            return counter
        for x,y in possiblepositions((a,b),board):
            if not visited[x][y]:
                visited[x][y] = True
                frontier.append((x,y,counter+1))
    return -1


n,m = map(int,input().split())
grid = [stdin.readline().strip() for i in range(n)]
print(minmoves(grid))
