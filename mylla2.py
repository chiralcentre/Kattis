def check_hjalti_win(board):
    # check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == "O":
            return "Jebb"
    # check columns
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == "O":
            return "Jebb"
    # check diagonals
    if board[0][0] == board[1][1] == board[2][2] == "O" or board[0][2] == board[1][1] == board[2][0] == "O":
        return "Jebb"
    return "Neibb"

board = [input().strip() for _ in range(3)]
print(check_hjalti_win(board))
