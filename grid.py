def possiblepositions(pos,board):
    k = board[pos[0]][pos[1]]
    movements = [(-k,0),(k,0),(0,-k),(0,k)]
    positions = []
    for x,y in movements:
        if pos[0] + x in range(len(board)) and pos[1] + y in range(len(board[0])):
            positions.append((pos[0] + x,pos[1] + y))
    return positions

def minmoves(board):
    r,c = len(board),len(board[0])
    # Sets are significantly faster when it comes to determining if an object is present in the structure, but are slower than lists during iteration
    visited = set((0,0)) #record positions visited before, starting from top left corner
    S = [((0,0),0)] # all possible neighbours we want to try
    # right coordinate keeps track of number of jumps
    while S:
        pos,counter = S.pop(0) #pop first element:
        if pos == (r-1,c-1):
            return counter
        pospn = possiblepositions(pos,board)
        for pn in pospn:
            if pn not in visited:
                visited.add(pn)
                S.append((pn,counter+1))
    return -1


n,m = list(map(int,input().split()))
grid = [list(map(int,list(input()))) for i in range(n)]
print(minmoves(grid))
