from sys import stdin,stdout

movements = {"u": (-1,0), "d": (1,0), "l": (0,-1), "r": (0,1)}
rotateRight = {"u": "r", "r": "d", "d": "l", "l": "u"}
rotateLeft = {"u": "l", "l": "d", "d": "r", "r": "u"}

def solve(grid,program):
    x,y,curr = 7,0,"r" # (x,y) is initial coordinates of turtle
    for m in program:
        if m == "R":
            curr = rotateRight[curr]
        elif m == "L":
            curr = rotateLeft[curr]
        elif m == "F":
            a,b = movements[curr]
            if 0 <= x + a <= 7 and 0 <= y + b <= 7 and grid[x + a][y + b] not in ["C","I"]:
                x += a; y += b
            else:
                return "Bug!"
        else: # X instruction
            a,b = movements[curr]
            a += x; b += y
            if 0 <= a <= 7 and 0 <= b <= 7 and grid[a][b] == "I":
                grid[a][b] = "."
            else:
                return "Bug!"
    return "Diamond!" if grid[x][y] == "D" else "Bug!"
        
    

grid = [list(stdin.readline().strip()) for _ in range(8)]
program = stdin.readline().strip()
stdout.write(solve(grid,program))
