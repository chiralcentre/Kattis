def shift(x,y):
    global grid
    #no directions unexplored
    if not grid[x][y]:
        return "no way out"
    #return direction to move into
    return grid[x][y].pop()
    
moves = {"down": (1,0), "up": (-1,0), "right": (0,1), "left": (0,-1)}
#every move has different priorities for subsequent moves, right end of list has higher priority
#follow left hand rule
p = {"down": ("up","left","right","down"), "up": ("down","right","left","up"),
     "right": ("left","down","up","right"), "left": ("right","down","up","left")}

#create a grid of size 201, start in middle position (100,100)
#grid[i][j] contains list of directions unexplored
grid = [[[] for i in range(201)] for j in range(201)]
x,y = 100,100
#start by moving in upwards direction
grid[x][y] = list(p["up"])
while True:
    d = shift(x,y)
    print(d)
    r = input().strip()
    if r == "solved" or r == "wrong":
        break
    elif r == "ok": #can move into that cell
        a,b = moves[d]
        x += a; y += b
        #new directions have not been put in yet
        if not grid[x][y]:
            grid[x][y] = list(p[d])
            
