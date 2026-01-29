from sys import stdin

movements = [(-1,-1),(-1,1),(1,1),(1,-1)]

def possiblepositions(i,j,r,c):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

r,c = map(int,stdin.readline().split())
s = int(stdin.readline())
field = [list(map(int,stdin.readline().split())) for _ in range(r)]
lucky = 0
for i in range(1,r - 1):
    for j in range(1, c - 1):
        if field[i][j] == s:
            total = sum(field[x][y] for x,y in possiblepositions(i,j,r,c))
            if not total % field[i][j]:
                lucky += 1
print(lucky)
            
    
