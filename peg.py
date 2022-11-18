from sys import stdin,stdout

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(0,1),(1,0),(0,-1)]
    return [((i+x,j+y),(i+2*x,j+2*y)) for x,y in movements if i + 2*x in range(r) and j + 2*y in range(c)]

board = [list(stdin.readline().strip("\n")) for _ in range(7)]
moves = 0
for i in range(7):
    for j in range(7):
        if board[i][j] == ".":
            for p1,p2 in possiblepositions(i,j,7,7):
                x1,y1 = p1; x2,y2 = p2
                if board[x1][y1] == "o" and board[x2][y2] == "o":
                    moves += 1
stdout.write(f"{moves}")
