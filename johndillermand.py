from sys import stdin,stdout

movements = [(-1,0),(0,1),(1,0),(0,-1)]
opposites = {"#": "O", "O": "#"}

def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c)]

h,w = map(int,stdin.readline().split())
frame = [list(stdin.readline().strip()) for _ in range(h)]
frontier = [(0,0)]
while frontier:
    i,j = frontier.pop()
    for x,y in possiblepositions(i,j,h,w,frame):
        if frame[x][y] == opposites[frame[i][j]]:
            frontier.append((x,y))
    frame[i][j] = "."
    
stdout.write("\n".join("".join(row) for row in frame))
