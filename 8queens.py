def possiblepositions(i,j,board):
    movements = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)] 
    positions = []
    for x,y in movements:
        row_sum, col_sum = 0,0
        for _ in range(len(board)):
            row_sum += x
            col_sum += y #increment every step
            if i + row_sum in range(len(board)) and j + col_sum in range(len(board[0])):
                positions.append((i + row_sum,j + col_sum))
            else: #out of range
                break
    return positions          

def eightqueens(board):
    queens = [(i,j) for i in range(len(board)) for j in range(len(board[0])) if board[i][j] == '*']
    if len(queens) != 8: #ensure number of queens = 8
        return 'invalid'
    for a,b in queens:
        pospn = possiblepositions(a,b,board)
        if len([value for value in queens if value in pospn]) > 0: #check for intersection
            return 'invalid'
    return 'valid'
               

print(eightqueens([list(input().strip()) for i in range(8)]))
