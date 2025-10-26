def find_winner(board):
    # iterate through all rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "E":
            return board[i][0]
    # iterate through all columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != "E":
            return board[0][j]
    # diagonals
    if (board[0][0] == board[1][1] == board[2][2] or
        board[0][2] == board[1][1] == board[2][0]) and board[1][1] != "E":
        return board[1][1]
    return "N"
board = [input().strip() for _ in range(3)]
print(find_winner(board))
