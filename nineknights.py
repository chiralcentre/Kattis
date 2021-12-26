transitions = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]
#test = ['.....','.....','..k..','.....','.....']

def possiblepositions(pos,board,movements):
    r,c = len(board),len(board[0])
    positions = []
    for x,y in movements:
        if pos[0] + x in range(r) and pos[1] + y in range(c):
            positions.append((pos[0] + x,pos[1] + y))
    return positions
           
def nineknights(board):
    r,c = len(board),len(board[0])
    knight_pos = []
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'k':
                knight_pos.append((i,j))
    # number of knights must be nine
    if len(knight_pos) != 9:
        return 'invalid'
    for knight in knight_pos:
        lst = possiblepositions(knight,board,transitions)
        for position in lst:
            if position in knight_pos:
                return 'invalid'
    return 'valid'    

print(nineknights([input().strip() for i in range(5)]))
