from sys import stdin,stdout
from heapq import heappush,heappop,heapify

def possiblepositions(i,j,r,c):
    movements = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

while True:
    h,w = map(int,stdin.readline().split()) #h is number of rows, w is number of columns
    if h == w == 0:
        break
    INF = 1000000000 # use 1 billion to represent infinity
    board = [list(stdin.readline().strip()) for _ in range(h)]
    D,p = [[INF for i in range(w)] for j in range(h)],[[(j,i) for i in range(w)] for j in range(h)] #keeps track of parent
    PQ = []
    for k in range(w):
        D[0][k] = int(board[0][k])
        PQ.append((D[0][k],0,k))
    heapify(PQ) #O(w) since there are w entries in PQ
    # modified Djikstra's is used with O(hw log hw) time complexity
    while PQ: 
        d,i,j = heappop(PQ)
        if d == D[i][j]:
            for x,y in possiblepositions(i,j,h,w):
                if D[x][y] > D[i][j] + int(board[x][y]):
                    D[x][y] = D[i][j] + int(board[x][y])
                    p[x][y] = (i,j)
                    heappush(PQ,(D[x][y],x,y))
    #find fracture line with minimum strength in O(w) time
    #D[i][j] stores minimum strength of fracture line from top edge to board[i][j]
    lowest,idx = INF,0
    for k in range(w):
        if D[h-1][k] < lowest:
            lowest = D[h-1][k]
            idx = k
    #backtrack with O(h) time complexity
    x,y = h-1,idx
    while p[x][y] != (x,y):
        board[x][y] = ' '
        x,y = p[x][y]
    board[x][y] = ' '
    stdout.write('\n'.join(''.join(row) for row in board)+'\n')
    stdout.write('\n') #print new line
        
