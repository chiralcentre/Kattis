from sys import stdin,stdout

def horizontalBound(board,OPTION):
    for j in (range(5 + 2*n) if OPTION == "L" else range(4 + 2*n, -1,-1)):
         for i in range(5 + 2*n):
             if board[i][j] != " ":
                 return j

def verticalBound(board,OPTION):
    for i in (range(5 + 2*n) if OPTION == "U" else range(4 + 2*n, -1,-1)):
         for j in range(5 + 2*n):
             if board[i][j] != " ":
                 return i
    
movements = {"up": (-1,0), "down": (1,0), "right": (0,1), "left": (0,-1)}  
while True:
    n = int(stdin.readline())
    if n == -1: break
    coordinates = {}
    board = [[" " for _ in range(5 + 2*n)] for i in range(5 + 2*n)]
    for i in range(n,n+5):
        for j in range(n,n+5):
            board[i][j] = chr(ord('A') + (i - n) * 5 + j - n)
            coordinates[board[i][j]] = (i,j)
    for _ in range(n):
        prev,d = stdin.readline().split()
        x,y = coordinates[prev]
        board[x][y] = " "; i,j = movements[d]
        nxt = board[x + i][y + j]
        if nxt == " ":
            board[x + i][y + j] = prev
            coordinates[prev] = (x + i,y + j)
        while nxt != " ":
            nxt = board[x + i][y + j]
            board[x + i][y + j] = prev
            coordinates[prev] = (x + i,y + j)
            x += i; y += j
            prev = nxt
    left,right = horizontalBound(board,"L"),horizontalBound(board,"R")
    top,bottom = verticalBound(board,"U"),verticalBound(board,"D")
    for i in range(top,bottom + 1):
        ans = "".join(char for char in [board[i][j] for j in range(left,right + 1)]).rstrip()
        stdout.write(f"{ans}\n")
    stdout.write("\n")
    
     
             
        
        
    
                
            
        
        
    
