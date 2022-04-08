from sys import stdin,stdout

def checkboard():
    N = int(stdin.readline())
    grid = [stdin.readline().strip() for _ in range(N)]
    for row in grid: #check rows
        B,W,consecutive,prev = 0,0,0,''
        for char in row:
            if char == 'B':
                B += 1
            else:
                W += 1
            if char != prev: #check for consecutive
                prev = char
                consecutive = 1
            else:
                consecutive += 1
                if consecutive >= 3:
                    return '0'
        if B != W:
            return '0'
    for i in range(N): #check columns
        B,W,consecutive,prev = 0,0,0,''
        for j in range(N):
            char = grid[j][i]
            if char == 'B':
                B += 1
            else:
                W += 1
            if char != prev: #check for consecutive
                prev = char
                consecutive = 1
            else:
                consecutive += 1
                if consecutive >= 3:
                    return '0'
        if B != W:
            return '0'
    return '1'

stdout.write(checkboard())
