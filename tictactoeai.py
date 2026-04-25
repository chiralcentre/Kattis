def solve(sym,board):
    # row by row
    for i in range(3):
        placed,empty = 0,[]
        for j in range(3):
            if board[i][j] == sym:
                placed += 1
            elif board[i][j] == "E":
                empty.append(j)
        if placed == 2 and len(empty) == 1:
            return f"{i + 1} {empty[0] + 1}"
    # column by column
    for j in range(3):
        placed,empty = 0,[]
        for i in range(3):
            if board[i][j] == sym:
                placed += 1
            elif board[i][j] == "E":
                empty.append(i)
        if placed == 2 and len(empty) == 1:
            return f"{empty[0] + 1} {j + 1}"
    # left diagonal
    placed,empty = 0,[]
    for i in range(3):
        if board[i][i] == sym:
            placed += 1
        elif board[i][i] == "E":
            empty.append(i)
    if placed == 2 and len(empty) == 1:
        return f"{empty[0] + 1} {empty[0] + 1}"
    # right diagonal
    placed,empty = 0,[]
    for i in range(3):
        if board[2 - i][i] == sym:
            placed += 1
        elif board[2 - i][i] == "E":
            empty.append(i)
    if placed == 2 and len(empty) == 1:
        return f"{3 - empty[0]} {empty[0] + 1}"
    raise Exception("not supposed to happen")

sym = input().strip()
board = [input().strip() for _ in range(3)]
print(solve(sym,board))
