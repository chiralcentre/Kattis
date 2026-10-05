def resolve(first,second,board):
    cross,circle = 0,0
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                cross += 1
            elif board[i][j] == "O":
                circle += 1
    # since cross player starts first, cross > circle and cross is at most 1 more than circle
    if circle > cross or cross > circle + 1:
        return "Invalid Game"
    cross_win,circle_win = 0,0
    # horizontal
    for i in range(3):
        cross_win += int(all(board[i][j] == "X" for j in range(3)))
        circle_win += int(all(board[i][j] == "O" for j in range(3)))
    # vertical
    for i in range(3):
        cross_win += int(all(board[j][i] == "X" for j in range(3)))
        circle_win += int(all(board[j][i] == "O" for j in range(3)))
    # right diagonal
    cross_win += int(all(board[i][i] == "X" for i in range(3)))
    circle_win += int(all(board[i][i] == "O" for i in range(3)))
    # left diagonal
    cross_win += int(all(board[2 - i][i] == "X" for i in range(3)))
    circle_win += int(all(board[2 - i][i] == "O" for i in range(3)))
    if cross_win + circle_win > 1:
        return "Invalid Game"
    if cross_win == 1:
        return first
    if circle_win == 1:
        return second
    if cross_win == circle_win == 0:
        return "Draw" if cross + circle == 9  else "In-Progress"
    
first,second = input().strip().split()
board = [input().strip() for _ in range(3)]
print(resolve(first,second,board))
