from sys import stdin

def treasurehunt(R,C,grid):
    row,col,counter = 0,0,0 
    visited = {(0,0)} #stores coordinates of visited places
    movements = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    while row in range(R) and col in range(C):
        move = grid[row][col]
        if move in movements:
            row += movements[move][0]
            col += movements[move][1]
            if (row,col) in visited:
                return 'Lost' #endless loop
            else:
                visited.add((row,col))
            counter += 1
        else: #treasure found
            return counter
    return 'Out'

R,C = map(int,stdin.readline().split())
print(treasurehunt(R,C,[stdin.readline() for _ in range(R)]))

