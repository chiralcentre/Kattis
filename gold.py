transitions = [(-1,0),(0,1),(1,0),(0,-1)]

def possiblepositions(pos,board,movements):
    r,c = len(board),len(board[0])
    positions = []
    for x,y in movements: # do not need to check for out of bounds due to border walls
        positions.append([pos[0] + x,pos[1] + y])
    return positions

def gold(board):
    r,c = len(board),len(board[0])
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'P':
                player = [i,j]
    visited = [player] #record positions visited before
    S = [player] # all possible neighbours we want to try
    counter = 0
    while S:
        pos = S.pop()
        pospn = possiblepositions(pos,board,transitions)
        trapped = False #check if position is surrounded by traps
        for x,y in pospn:
            if board[x][y] == 'T':
                trapped = True
        if trapped == False:
            for x,y in pospn:
                if board[x][y] != '#' and [x,y] not in visited:
                    visited.append([x,y])
                    S.append([x,y])
                    if board[x][y] == 'G':
                        counter += 1
    return counter


n = list(map(int,input().split()))
h,w = n[1],n[0]
grid = []
for i in range(h):
    grid.append(input().strip())

print(gold(grid))
