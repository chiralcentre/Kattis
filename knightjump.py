transitions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

def possiblepositions(pos,board,movements):
    r,c = len(board),len(board[0])
    positions = []
    for x,y in movements:
        if pos[0] + x in range(r) and pos[1] + y in range(c):
            positions.append((pos[0] + x,pos[1] + y))
    return positions
    
#tuples worked and not lists
def minsteps(board):
    r,c = len(board),len(board[0]) 
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'K':
                knight = (i,j)
    visited = [knight] #record positions visited before
    S = [(knight,0)] # all possible neighbours we want to try
    # right coordinate keeps track of number of jumps
    while S:
        pos,counter = S.pop(0) #pop first element
        if pos == (0,0):
            return counter
        pospn = possiblepositions(pos,board,transitions)
        for x,y in pospn:
            if board[x][y] != '#' and (x,y) not in visited:
                visited.append((x,y))
                S.append(((x,y),counter + 1))
    return -1

n = int(input())
chessboard = []
for i in range(n):
    line = input().strip()
    chessboard.append(line)
    
print(minsteps(chessboard))



