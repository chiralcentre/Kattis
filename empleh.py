columns = {'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}

W = input().strip().split(":")[1].strip().split(",")
B = input().strip().split(":")[1].strip().split(",")
board = [["" for i in range(8)] for j in range(8)]
for s in W:
    if len(s) == 3: #not pawn
        c,r = columns[s[1]],8 - int(s[2])
        board[r][c] = s[0]
    elif len(s) == 2: #pawn
        c,r = columns[s[0]],8 - int(s[1])
        board[r][c] = "P"
for s in B:
    if len(s) == 3: #not pawn
        c,r = columns[s[1]],8 - int(s[2])
        board[r][c] = s[0].lower()
    elif len(s) == 2: #pawn
        c,r = columns[s[0]],8 - int(s[1])
        board[r][c] = "p"

print("+---+---+---+---+---+---+---+---+")
for i in range(8):
    print("|", end = "")
    for j in range(8):
        sep = ":" if (i + j) % 2 else "."
        print(sep, end = "")
        print(board[i][j], end = "") if board[i][j] else print(sep, end = "")
        print(sep + "|", end = "")
    print() #new line
    print("+---+---+---+---+---+---+---+---+")
