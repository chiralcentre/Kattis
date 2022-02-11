from collections import deque
# Credit to Dr Chong Ket Fah for the idea
# Main idea: generate all possible ending patterns, and save those patterns along with clicks needed to generate them in a dictionary
# Use BFS to find number of clicks required to generate a pattern 
def possiblepositions(i,j,board):
    movements = [(-1,0),(0,1),(0,0),(1,0),(0,-1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(len(board)) and j + y in range(len(board[0]))]

positions = [(i,j) for i in range(3) for j in range(3)] # store square coordinates
visited = {(('.','.','.'),('.','.','.'),('.','.','.')):0}
frontier = deque([((('.','.','.'),('.','.','.'),('.','.','.')),0)]) # right coordinate keeps track of number of moves
# necessary to convert between tuple and list as dictionary keys must be immutable
while frontier: 
    grid,counter = frontier.popleft()
    for i,j in positions: #BFS
        grid2 = [list(row) for row in grid] #deepcopy
        for x,y in possiblepositions(i,j,grid2):
            grid2[x][y] = '*' if grid2[x][y] == '.' else '.'
        grid3 = tuple([tuple(row) for row in grid2]) 
        if grid3 not in visited: # a dictionary is used so that the in operator has O(1) time complexity
            visited[grid3] = counter + 1
            frontier.append((grid3,counter + 1))
            
for i in range(int(input())):
    given_grid = tuple(list(tuple(input().strip()) for j in range(3)))
    print(visited[given_grid])
