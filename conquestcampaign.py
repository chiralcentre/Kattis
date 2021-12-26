def possiblepositions(i,j,board):
    movements = [(-1,0),(1,0),(0,-1),(0,1)]
    return [(i+x,j+y) for x,y in movements if i + x in range(len(board)) and j + y in range(len(board[0]))]

R,C,N = list(map(int,input().split()))
country = [[0 for j in range(C)] for i in range(R)]
cells = set()

for k in range(N):
    coordinates = tuple(map(lambda x: x - 1, map(int,input().split())))
    if coordinates not in cells:
        cells.add(coordinates)
        country[coordinates[0]][coordinates[1]] = 1
    
days,counter = 1,len(cells)
while counter < R*C:
    occupied = list(cells)
    for x,y in occupied:
        pospn = possiblepositions(x,y,country)
        for c,d in pospn:
            if not country[c][d]:
                country[c][d] = 1
                counter += 1
                cells.add((c,d))
    days += 1

print(days)
                
        
    
        
        
        
    
