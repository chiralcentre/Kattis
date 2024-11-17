from sys import stdin

movements = [(-1,0),(0,1),(1,0),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]
def possiblepositions(i,j,r,c,grid):
    return [(i+x,j+y) for x,y in movements if i + x in range(r) and j + y in range(c) and grid[i + x][j + y] == "O"]

r,c = map(int,stdin.readline().split())
grid = [stdin.readline().strip() for _ in range(r)]
ans = []
for i in range(r):
    for j in range(c):
        if grid[i][j] == "0" and len(possiblepositions(i,j,r,c,grid)) == 8:
            ans.append((i + 1, j + 1))
if not ans:
    print("Oh no!")
elif len(ans) == 1:
    print(f"{ans[0][0]} {ans[0][1]}")
else:
    print(f"Oh no! {len(ans)} locations")
