def adjacentseats(pos,board,r,c):
    movements = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    adj = 0
    for x,y in movements:
        if pos[0] + x in range(r) and pos[1] + y in range(c) and board[pos[0]+x][pos[1]+y] == 1:
            adj += 1
    return adj

R,C = list(map(int,input().split()))
cinema = [[0 for i in range(C)] for j in range(R)]

N = int(input())
for k in range(N):
    x,y = list(map(lambda x: x - 1, map(int,input().split())))
    cinema[x][y] = 1

lst = [0,0,0,0,0,0,0,0,0]
for i in range(R):
    for j in range(C):
        if cinema[i][j] == 1:
            lst[adjacentseats((i,j),cinema,R,C)] += 1
print(' '.join(map(str,lst)))
            
        


