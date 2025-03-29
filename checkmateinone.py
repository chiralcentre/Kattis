directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def get_position(board,char):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == char:
                return (i,j)
    raise Exception("character not present in chessboard")

def in_range(x,y):
    return 0 <= x < 8 and 0 <= y < 8

def check_square(grid,x,y):
    # check for kings
    for i in range(-1, 2):
        for j in range(-1, 2):
            if in_range(x + i, y + j) and grid[x + i][y + j] == 'K':
                return False
    # check for rooks
    for a,b in directions:
        c,d = x,y
        while in_range(c + a,d + b):
            c += a
            d += b
            if grid[c][d] == "R":
                return False
            if grid[c][d] == "K":
                break
    return True

def safe(grid,opp_king):
    x,y = opp_king
    ok = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if in_range(x + i, y + j):
                old = grid[x + i][y + j]
                grid[x + i][y + j] = '.'
                grid[x][y] = '.'
                ok = ok or check_square(grid, x + i, y + j)
                grid[x][y] = 'k'
                grid[x + i][y + j] = old
    return ok

def check(grid,x,y,opp_king):
    grid[x][y] = '.'
    for dx, dy in directions:
        newx, newy = x + dx, y + dy
        while in_range(newx,newy) and grid[newx][newy] == ".":
            grid[newx][newy] = 'R'
            if not safe(grid,opp_king):
                return True
            grid[newx][newy] = '.'
            newx += dx
            newy += dy
    grid[x][y] = 'R'
    return False

def main():
    grid = [list(input().strip()) for _ in range(8)]
    own_rook = get_position(grid,"R")
    opp_king = get_position(grid,"k")
    print("Yes" if check(grid,own_rook[0],own_rook[1],opp_king) else "No")

if __name__ == "__main__":
    main()
