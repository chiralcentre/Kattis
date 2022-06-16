from sys import stdin,stdout
from collections import deque

def BFS(grid):
    end = ((0,0,0),(0,0,0),(0,0,0))
    visited = {grid}
    frontier = deque([(grid,0)])
    while frontier:
        state,moves = frontier.popleft()
        for i in range(3):
            for j in range(3):
                temp = [list(row) for row in state]
                #increment digits in same row
                for k in range(3):
                    temp[i][k] += 1
                    temp[i][k] %= 4
                #increment digits in same column, but prevent double counting
                for m in range(3):
                    if m != i:
                        temp[m][j] += 1
                        temp[m][j] %= 4
                result = tuple(tuple(row) for row in temp)
                if result == end:
                    return str(moves+1)
                if result not in visited:
                    visited.add(result)
                    frontier.append((result,moves+1))
    return "-1" #impossible to reach end state

grid = tuple(tuple(map(int,stdin.readline().split())) for i in range(3))
stdout.write(BFS(grid))
            
            
            
