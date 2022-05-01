from sys import stdin,stdout

def checkBlankColumn(N,j,grid):
    for i in range(N):
        if grid[i][j] != '_':
            return 0
    return 1

N,M = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(N)]
#count number of blank columns + 1 since there is 1 blank column between two moves
stdout.write(f'{sum(checkBlankColumn(N,j,grid) for j in range(M)) + 1}')
        
            
